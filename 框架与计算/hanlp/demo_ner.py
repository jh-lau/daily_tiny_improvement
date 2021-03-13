"""
  @Author       : liujianhan
  @Date         : 2020/1/9 下午2:58
  @Project      : DailyTinyImprovement
  @FileName     : demo_ner.py
  @Description  : Placeholder
"""

import hanlp

recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_ALBERT_BASE_ZH)
print(recognizer.predict([list('上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。'),
                          list('萨哈夫说，伊拉克将同联合国销毁伊拉克大规模杀伤性武器特别委员会继续保持合作。')]))
