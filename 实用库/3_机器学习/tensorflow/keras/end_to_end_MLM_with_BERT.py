"""
  @Author       : liujianhan
  @Date         : 21/7/15 22:09
  @Project      : DailyTinyImprovement
  @FileName     : end_to_end_MLM_with_BERT.py
  @Description  : placeholder
"""
import tensorflow as tf
from dataclasses import dataclass
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import pandas as pd
import numpy as np
import glob
import re
from pprint import pprint


@dataclass
class Config:
    MAX_LEN = 256
    BATCH_SIZE = 32
    LR = .001
    VOCAB_SIZE = 30000
    EMBED_DIM = 128
    NUM_HEAD = 8
    FF_DIM = 128
    NUM_LAYERS = 1


def get_text_list_from_files(files):
    text_list = []
    for name in files:
        with open(name, encoding='utf8') as f:
            for line in f:
                text_list.append(line)
    return text_list


def get_data_from_text_files(folder_name):
    pos_files = glob.glob(f'{folder_name}/pos/*.txt')
    pos_texts = get_text_list_from_files(pos_files)
    neg_files = glob.glob(f'{folder_name}/neg/*.txt')
    neg_texts = get_text_list_from_files(neg_files)
    df = pd.DataFrame(
        {
            'review': pos_texts + neg_texts,
            'sentiment': [0] * len(pos_texts) + [1] * len(neg_texts),
        }
    )
    df = df.sample(len(df)).reset_index(drop=True)
    return df


def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, "<br />", " ")
    return tf.strings.regex_replace(
        stripped_html, "[%s]" % re.escape("!#$%&'()*+,-./:;<=>?@\^_`{|}~"), ""
    )


def get_vectorize_layer(texts, vocab_size, max_seq, special_tokens=None):
    if special_tokens is None:
        special_tokens = ['[MASK]']
    vectorize_layer = TextVectorization(
        max_tokens=vocab_size,
        output_mode='int',
        standardize=custom_standardization,
        output_sequence_length=max_seq
    )
    vectorize_layer.adapt(texts)
    vocab = vectorize_layer.get_vocabulary()
    vocab = vocab[2: vocab_size - len(special_tokens)] + ['[mask]']
    vectorize_layer.set_vocabulary(vocab)
    return vectorize_layer


def encode(vectorize_layer, texts):
    encoded_texts = vectorize_layer(texts)
    return encoded_texts.numpy()


def get_masked_input_and_labels(encoded_texts, mask_token_id):
    inp_mask = np.random.rand(*encoded_texts.shape) < .15  # 15% BERT masking
    inp_mask[encoded_texts <= 2] = False  # do not mask special tokens: padding、unknown、mask
    labels = -1 * np.ones(encoded_texts.shape, dtype=int)  # -1 means ignore
    labels[inp_mask] = encoded_texts[inp_mask]  # set labels for masked tokens

    encoded_texts_masked = np.copy(encoded_texts)
    # 输入的mask15%中的90%进行mask，另外10%保持原来token
    inp_mask_2mask = inp_mask & (np.random.rand(*encoded_texts.shape) < .9)
    encoded_texts_masked[inp_mask_2mask] = mask_token_id
    # 90%中的1/9使用其他token替换，8/9使用mask_token替换
    inp_mask_2random = inp_mask_2mask & (np.random.rand(*encoded_texts.shape) < 1 / 9)
    encoded_texts_masked[inp_mask_2random] = np.random.randint(
        3, mask_token_id, inp_mask_2random.sum()
    )
    sample_weights = np.ones(labels.shape)
    sample_weights[labels == -1] = 0
    y_labels = np.copy(encoded_texts)
    return encoded_texts_masked, y_labels, sample_weights


def bert_module(query, key, value, i):
    attention_output = layers.MultiHeadAttention(
        num_heads=config.NUM_HEAD,
        key_dim=config.EMBED_DIM // config.NUM_HEAD,
        name=f"encoder_{i}/multi_head_attention"
    )(query, key, value)
    attention_output = layers.Dropout(.1, name=f"encoder_{i}/att_dropout")(attention_output)
    attention_output = layers.LayerNormalization(
        epsilon=1e-6, name=f"encoder_{i}/att_layer_normalization"
    )(query + attention_output)

    ffn = keras.Sequential(
        [
            layers.Dense(config.FF_DIM, activation='relu'),
            layers.Dense(config.EMBED_DIM),
        ],
        name=f"encoder_{i}/ffn",
    )
    ffn_output = ffn(attention_output)
    ffn_output = layers.Dropout(.1, name=f'encoder_{i}/ffn_dropout')(ffn_output)
    sequence_output = layers.LayerNormalization(
        epsilon=1e-6, name=f"encoder_{i}/ffn_layer_normalization"
    )(attention_output + ffn_output)

    return sequence_output


def get_pos_encoding_matrix(max_len, d_emb):
    pos_enc = np.array(
        [
            [pos / np.power(10000, 2 * (j // 2) / d_emb) for j in range(d_emb)]
            if pos != 0 else np.zeros(d_emb) for pos in range(max_len)
        ]
    )
    pos_enc[1:, 0::2] = np.sin(pos_enc[1:, 0::2])
    pos_enc[1:, 1::2] = np.cos(pos_enc[1:, 1::2])
    return pos_enc


class MaskedLanguageModel(keras.Model):
    def train_step(self, inputs):
        if len(inputs) == 3:
            features, labels, sample_weight = inputs
        else:
            features, labels = inputs
            sample_weight = None
        with tf.GradientTape() as tape:
            predictions = self(features, training=True)
            loss = self.compiled_loss(labels, predictions, sample_weight=sample_weight)

        gradients = tape.gradient(loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))
        # todo: wrong with self.compiled_metric on keras.metrics.MEAN(name='loss')
        # self.compiled_metric会调用update_state，该函数的签名为y_true, y_pred, sample_weight
        # 如果传入的metrics不是这么个用法，如loss_tracker，就没法这么写
        loss_tracker.update_state(loss, sample_weight=sample_weight)
        return {'loss': loss_tracker.result()}

    @property
    def metrics(self):
        return [loss_tracker]


def create_masked_language_bert_model():
    inputs = layers.Input((config.MAX_LEN,), dtype=tf.int64)

    word_embedding = layers.Embedding(
        config.VOCAB_SIZE, config.EMBED_DIM, name='word_embedding'
    )(inputs)
    position_embeddings = layers.Embedding(
        input_dim=config.MAX_LEN,
        output_dim=config.EMBED_DIM,
        weights=[get_pos_encoding_matrix(config.MAX_LEN, config.EMBED_DIM)],
        name='position_embedding'
    )(tf.range(start=0, limit=config.MAX_LEN, delta=1))
    embeddings = word_embedding + position_embeddings

    encoder_output = embeddings
    for i in range(config.NUM_LAYERS):
        encoder_output = bert_module(encoder_output, encoder_output, encoder_output, i)
    mlm_output = layers.Dense(config.VOCAB_SIZE, name='mlm_cls', activation='softmax')(encoder_output)
    mlm_model = MaskedLanguageModel(inputs, mlm_output, name='masked_bert_model')
    mlm_model.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(reduction=keras.losses.Reduction.NONE),
        # metrics=[keras.metrics.Mean(name='loss')],
        optimizer=keras.optimizers.Adam(learning_rate=config.LR)
    )

    return mlm_model


class MaskedTextGenerator(keras.callbacks.Callback):
    def __init__(self, sample_tokens, mask_token_id, id2token, top_k=5):
        self.sample_tokens = sample_tokens
        self.k = top_k
        self.id2token = id2token
        self.mask_token_id = mask_token_id

    def decode(self, tokens):
        return " ".join([self.id2token[t] for t in tokens if t != 0])

    def convert_ids_to_tokens(self, _id):
        return self.id2token[_id]

    def on_epoch_end(self, epoch, logs=None):
        prediction = self.model.predict(self.sample_tokens)
        masked_index = np.where(self.sample_tokens == self.mask_token_id)
        masked_index = masked_index[1]
        mask_prediction = prediction[0][masked_index]

        top_indices = mask_prediction[0].argsort()[-self.k:][::-1]
        values = mask_prediction[0][top_indices]

        for i in range(len(top_indices)):
            p = top_indices[i]
            v = values[i]
            tokens = np.copy(self.sample_tokens[0])
            tokens[masked_index[0]] = p
            result = {
                'input_text': self.decode(self.sample_tokens[0].numpy()),
                'prediction': self.decode(tokens),
                'probability': v,
                'predicted mask token': self.convert_ids_to_tokens(p)
            }
            pprint(result)


if __name__ == '__main__':
    config = Config()
    loss_tracker = keras.metrics.Mean(name="loss")
    train_folder = r'C:\Users\MeetYou\Downloads\aclImdb_v1\aclImdb\train'
    test_folder = r'C:\Users\MeetYou\Downloads\aclImdb_v1\aclImdb\test'
    train_df = get_data_from_text_files(train_folder)
    test_df = get_data_from_text_files(test_folder)
    all_data = train_df.append(test_df)
    vectorize_layer = get_vectorize_layer(
        all_data.review.values.tolist(),
        config.VOCAB_SIZE,
        config.MAX_LEN,
        special_tokens=['[mask]'],
    )
    mask_token_id = vectorize_layer(['[mask]']).numpy()[0][0]
    x_train = encode(vectorize_layer, train_df.review.values)
    y_train = train_df.sentiment.values
    train_classifier_ds = (
        tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(1000).batch(config.BATCH_SIZE)
    )
    x_test = encode(vectorize_layer, test_df.review.values)
    y_test = test_df.sentiment.values
    test_classifier_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(config.BATCH_SIZE)
    # end to end model input
    test_raw_classifier_ds = tf.data.Dataset.from_tensor_slices(
        (test_df.review.values, y_test)
    ).batch(config.BATCH_SIZE)
    x_all_review = encode(vectorize_layer, all_data.review.values)
    x_masked_train, y_masked_labels, sample_weights = get_masked_input_and_labels(x_all_review, mask_token_id)
    mlm_ds = tf.data.Dataset.from_tensor_slices((x_masked_train, y_masked_labels, sample_weights))
    mlm_ds = mlm_ds.shuffle(1000).batch(config.BATCH_SIZE)

    id2token = dict(enumerate(vectorize_layer.get_vocabulary()))
    token2id = {y: x for x, y in id2token.items()}
    sample_tokens = vectorize_layer(['I have watched this [mask] and it was awesome'])
    generator_callback = MaskedTextGenerator(sample_tokens.numpy(), mask_token_id, id2token)

    bert_masked_model = create_masked_language_bert_model()
    # bert_masked_model.summary()
    # keras.utils.plot_model(bert_masked_model, to_file='bert_masked_model.png', show_shapes=True)
    bert_masked_model.fit(mlm_ds, epochs=5, callbacks=[generator_callback])
    bert_masked_model.save('./model/bert_mlm_imbd.h5')
