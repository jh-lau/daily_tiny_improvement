"""
  @Author       : liujianhan
  @Date         : 2021/7/19 11:53
  @Project      : DailyTinyImprovement
  @FileName     : end_to_end_MLM_with_BERT.py
  @Description  : Placeholder
"""
from transformers import BertTokenizer, BertModel, pipeline
import os
os.environ['USE_TF'] = True

if __name__ == '__main__':
    print('Start loading...')
    # tokenizer = BertTokenizer.from_pretrained(r'D:\Projects\pretrained_models\chinese_roberta_wwm_ext_L-12_H-768_A-12_torch')
    model = BertModel.from_pretrained(r'D:\Projects\pretrained_models\chinese_roberta_wwm_ext_L-12_H-768_A-12_torch')
    print("Done")
