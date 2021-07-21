"""
  @Author       : liujianhan
  @Date         : 2021/7/20 9:18
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  : 支持tf+keras和tf+tf.keras，后者需要提前传入环境变量TF_KERAS=1。
    当使用tf+keras时，建议2.2.4 <= keras <= 2.3.1，以及 1.14 <= tf <= 2.2，不能使用tf 2.3+。
    keras 2.4+可以用，但事实上keras 2.4.x基本上已经完全等价于tf.keras了，因此如果你要用keras 2.4+，倒不如直接用tf.keras。
"""
import os

os.environ['TF_KERAS'] = '1'
from bert4keras.models import build_transformer_model
from bert4keras.tokenizers import Tokenizer
import numpy as np

if __name__ == '__main__':
    config_path = 'D:/Projects/pretrained_models/chinese_roberta_wwm_ext_L-12_H-768_A-12/config.json'
    checkpoint_path = 'D:/Projects/pretrained_models/chinese_roberta_wwm_ext_L-12_H-768_A-12/bert_model.ckpt'
    dict_path = 'D:/Projects/pretrained_models/chinese_roberta_wwm_ext_L-12_H-768_A-12/vocab.txt'

    tokenizer = Tokenizer(dict_path, do_lower_case=True)  # 建立分词器
    model = build_transformer_model(config_path, checkpoint_path)  # 建立模型，加载权重

    # 编码测试
    token_ids, segment_ids = tokenizer.encode(u'语言模型')

    print('\n ===== predicting =====\n')
    print(model.predict([np.array([token_ids]), np.array([segment_ids])]))
