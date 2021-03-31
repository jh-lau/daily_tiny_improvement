"""
  @Author       : liujianhan
  @Date         : 2020/1/9 下午3:20
  @Project      : DailyTinyImprovement
  @FileName     : demo_pos.py
  @Description  : Placeholder
"""
import hanlp
from hanlp.pretrained.pos import CTB5_POS_RNN_FASTTEXT_ZH
tagger = hanlp.load(CTB5_POS_RNN_FASTTEXT_ZH)
print(tagger.predict(['我', '的', '希望', '是', '希望', '和平']))
print(tagger.predict([['支持', '批处理'], ['速度', '更', '快']]))