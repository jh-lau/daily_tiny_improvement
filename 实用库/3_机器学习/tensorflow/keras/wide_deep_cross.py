"""
  @Author       : liujianhan
  @Date         : 21/6/30 22:23
  @Project      : DailyTinyImprovement
  @FileName     : wide_deep_cross.py
  @Description  : Placeholder
"""
import math
import time

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import classification_report
from tensorflow import keras
from tensorflow.keras import layers


def get_dataset_from_csv(csv_file_path, batch_size, shuffle=False):
    dataset = tf.data.experimental.make_csv_dataset(
        csv_file_path,
        batch_size=batch_size,
        column_names=CSV_HEADER,
        column_defaults=COLUMN_DEFAULTS,
        label_name=TARGET_FEATURE_NAME,
        num_epochs=1,
        header=True,
        shuffle=shuffle,
    )
    return dataset.cache()


def create_model_inputs():
    inputs = {}
    for feature_name in FEATURE_NAMES:
        if feature_name in NUMERIC_FEATURE_NAMES:
            inputs[feature_name] = layers.Input(
                name=feature_name, shape=(), dtype=tf.float32
            )
        else:
            inputs[feature_name] = layers.Input(
                name=feature_name, shape=(), dtype=tf.string
            )
    return inputs


def encode_inputs(inputs, use_embedding=False):
    encoded_features = []
    for feature_name in inputs:
        if feature_name in CATEGORICAL_FEATURE_NAMES:
            vocabulary = CATEGORICAL_FEATURES_WITH_VOCABULARY[feature_name]
            lookup = layers.experimental.preprocessing.StringLookup(
                vocabulary=vocabulary,
                mask_token=None,
                num_oov_indices=0,
                output_mode="int" if use_embedding else "binary",
            )
            if use_embedding:
                # Convert the string input values into integer indices.
                encoded_feature = lookup(inputs[feature_name])
                embedding_dims = int(math.sqrt(len(vocabulary)))
                # Create an embedding layer with the specified dimensions.
                embedding = layers.Embedding(
                    input_dim=len(vocabulary), output_dim=embedding_dims
                )
                # Convert the index values to embedding representations.
                encoded_feature = embedding(encoded_feature)
            else:
                # Convert the string input values into a one hot encoding.
                encoded_feature = lookup(tf.expand_dims(inputs[feature_name], -1))
        else:
            # Use the numerical features as-is.
            encoded_feature = tf.expand_dims(inputs[feature_name], -1)

        encoded_features.append(encoded_feature)

    all_features = layers.concatenate(encoded_features)
    return all_features


def create_baseline_model():
    inputs = create_model_inputs()
    features = encode_inputs(inputs)

    for units in hidden_units:
        features = layers.Dense(units)(features)
        features = layers.BatchNormalization()(features)
        features = layers.ReLU()(features)
        features = layers.Dropout(dropout_rate)(features)

    outputs = layers.Dense(units=NUM_CLASSES, activation="softmax")(features)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model


def create_wide_and_deep_model():
    inputs = create_model_inputs()
    wide = encode_inputs(inputs)
    wide = layers.BatchNormalization()(wide)

    deep = encode_inputs(inputs, use_embedding=True)
    for units in hidden_units:
        deep = layers.Dense(units)(deep)
        deep = layers.BatchNormalization()(deep)
        deep = layers.ReLU()(deep)
        deep = layers.Dropout(dropout_rate)(deep)

    merged = layers.concatenate([wide, deep])
    outputs = layers.Dense(units=NUM_CLASSES, activation="softmax")(merged)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model


def create_deep_and_cross_model():
    inputs = create_model_inputs()
    x0 = encode_inputs(inputs, use_embedding=True)

    cross = x0
    for _ in hidden_units:
        units = cross.shape[-1]
        x = layers.Dense(units)(cross)
        cross = x0 * x + cross
    cross = layers.BatchNormalization()(cross)

    deep = x0
    for units in hidden_units:
        deep = layers.Dense(units)(deep)
        deep = layers.BatchNormalization()(deep)
        deep = layers.ReLU()(deep)
        deep = layers.Dropout(dropout_rate)(deep)

    merged = layers.concatenate([cross, deep])
    outputs = layers.Dense(units=NUM_CLASSES, activation="softmax")(merged)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model


class CustomMetricsCallback(keras.callbacks.Callback):
    def __init__(self, valid_test_data):
        super().__init__()
        self.dataset = valid_test_data

    def classification_report(self):
        y_true = []
        y_pred = []
        t1 = time.time()
        for i, (data, label) in enumerate(self.dataset):
            y_pred.extend(np.argmax(self.model.predict(data), -1))
            y_true.extend(label.numpy().tolist())
        print(classification_report(y_true, y_pred, zero_division=0, digits=4))
        print(f'评估耗时：{time.time() - t1: .3f} 秒')
        return

    def on_test_end(self, epoch, logs=None):
        self.classification_report()

    def on_epoch_end(self, epoch, logs=None):
        print(
            epoch
        )
        self.classification_report()


def run_experiment(model):
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss=keras.losses.SparseCategoricalCrossentropy(),
        metrics=[keras.metrics.SparseCategoricalAccuracy()],
    )
    train_dataset = get_dataset_from_csv(train_data_file, batch_size, shuffle=True)

    eval_dataset = get_dataset_from_csv(eval_data_file, batch_size + 1280)
    test_dataset = get_dataset_from_csv(test_data_file, batch_size + 1280)
    eval_metric_callback = CustomMetricsCallback(eval_dataset)
    test_metric_callback = CustomMetricsCallback(test_dataset)

    print("Start training the model...")
    model.fit(train_dataset, epochs=num_epochs, callbacks=[eval_metric_callback])
    # model.fit(train_dataset, epochs=num_epochs)
    print("Model training finished")

    _, accuracy = model.evaluate(test_dataset, verbose=0, callbacks=[test_metric_callback])

    print(f"Test accuracy: {round(accuracy * 100, 2)}%")


if __name__ == '__main__':
    CSV_HEADER = [
        "Elevation",
        "Aspect",
        "Slope",
        "Horizontal_Distance_To_Hydrology",
        "Vertical_Distance_To_Hydrology",
        "Horizontal_Distance_To_Roadways",
        "Hillshade_9am",
        "Hillshade_Noon",
        "Hillshade_3pm",
        "Horizontal_Distance_To_Fire_Points",
        "Wilderness_Area",
        "Soil_Type",
        "Cover_Type",
    ]
    data = pd.read_csv('data/covtype_data/eval/covtype_eval.csv')
    train_data_file = tf.io.gfile.glob('data/covtype_data/eval/*.csv')
    eval_data_file = tf.io.gfile.glob('data/covtype_data/eval/*.csv')
    test_data_file = tf.io.gfile.glob('data/covtype_data/eval/*.csv')

    # data_path = 'data/covtype_data.csv'
    # train_data_file = 'data/covtype_train.csv'
    # test_data_file = 'data/covtype_eval.csv'
    # raw_data = pd.read_csv(data_path, header=None)
    # print(f"dataset shape: {raw_data.shape}")
    # soil_type_values = [f"soil_type_{idx + 1}" for idx in range(40)]
    # wilderness_area_values = [f"area_type_{idx + 1}" for idx in range(4)]
    # soil_type = raw_data.loc[:, 14:53].apply(
    #     lambda x: soil_type_values[0::1][x.to_numpy().nonzero()[0][0]], axis=1
    # )
    # wilderness_area = raw_data.loc[:, 10:13].apply(
    #     lambda x: wilderness_area_values[0::1][x.to_numpy().nonzero()[0][0]], axis=1
    # )
    # data = pd.concat(
    #     [raw_data.loc[:, 0:9], wilderness_area, soil_type, raw_data.loc[:, 54]],
    #     axis=1,
    #     ignore_index=True,
    # )
    # data.columns = CSV_HEADER
    # # Convert the target label indices into a range from 0 to 6 (there are 7 labels in total).
    # data["Cover_Type"] = data["Cover_Type"] - 1
    # print(f"Dataset shape: {data.shape}")
    # train_splits = []
    # test_splits = []
    # # 从每种类型中抽取部分保证分布的一致性
    # for _, group_data in data.groupby("Cover_Type"):
    #     random_selection = np.random.rand(len(group_data.index)) <= 0.85
    #     train_splits.append(group_data[random_selection])
    #
    # train_data = pd.concat(train_splits).sample(frac=1).reset_index(drop=True)
    # test_data = pd.concat(test_splits).sample(frac=1).reset_index(drop=True)
    # print(f"Train split size: {len(train_data.index)}")
    # print(f"Test split size: {len(test_data.index)}")
    # train_data.to_csv(train_data_file, index=False)
    # test_data.to_csv(test_data_file, index=False)

    TARGET_FEATURE_NAME = "Cover_Type"
    TARGET_FEATURE_LABELS = ["0", "1", "2", "3", "4", "5", "6"]
    NUMERIC_FEATURE_NAMES = [
        "Aspect",
        "Elevation",
        "Hillshade_3pm",
        "Hillshade_9am",
        "Hillshade_Noon",
        "Horizontal_Distance_To_Fire_Points",
        "Horizontal_Distance_To_Hydrology",
        "Horizontal_Distance_To_Roadways",
        "Slope",
        "Vertical_Distance_To_Hydrology",
    ]

    CATEGORICAL_FEATURES_WITH_VOCABULARY = {
        "Soil_Type": list(data["Soil_Type"].unique()),
        "Wilderness_Area": list(data["Wilderness_Area"].unique()),
    }

    CATEGORICAL_FEATURE_NAMES = list(CATEGORICAL_FEATURES_WITH_VOCABULARY.keys())

    FEATURE_NAMES = NUMERIC_FEATURE_NAMES + CATEGORICAL_FEATURE_NAMES

    COLUMN_DEFAULTS = [
        [0] if feature_name in NUMERIC_FEATURE_NAMES + [TARGET_FEATURE_NAME] else ["NA"]
        for feature_name in CSV_HEADER
    ]

    NUM_CLASSES = len(TARGET_FEATURE_LABELS)
    learning_rate = 0.001
    dropout_rate = 0.1
    batch_size = 265
    num_epochs = 2

    hidden_units = [32, 32]
    flag = 3
    if flag == 1:
        baseline_model = create_baseline_model()
        # keras.utils.plot_model(baseline_model, show_shapes=True, rankdir="LR")
        run_experiment(baseline_model)
    elif flag == 2:
        wide_and_deep_model = create_wide_and_deep_model()
        # keras.utils.plot_model(wide_and_deep_model, show_shapes=True, rankdir="LR")
        run_experiment(wide_and_deep_model)
    elif flag == 3:
        deep_and_cross_model = create_deep_and_cross_model()
        tf.keras.utils.plot_model(deep_and_cross_model)
        # keras.utils.plot_model(deep_and_cross_model, show_shapes=True, rankdir="LR")
        # run_experiment(deep_and_cross_model)
