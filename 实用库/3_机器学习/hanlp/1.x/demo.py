"""
  @Author       : liujianhan
  @Date         : 21/8/3 19:57
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  : Placeholder
"""
from pyhanlp import *
CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
# StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")
# StandardTokenizer.SEGMENT.enableAllNamedEntityRecognize(True)
CustomDictionary.add("排卵")  # 动态增加
# CustomDictionary.add("排卵监测仪")  # 动态增加
CustomDictionary.add("美国绿卡")  # 动态增加

if __name__ == '__main__':
    # print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
    # for term in HanLP.segment('下雨天地面积水'):
    #     print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性
    testCases = [
        "商品和服务",
        "结婚的和尚未结婚的确实在干扰分词啊",
        "买水果然后来世博园最后去世博会",
        "中国的首都是北京",
        "欢迎新老师生前来就餐",
        "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
        "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。",
        "90后天才少年曹原，世界难题我都攻克了，还会稀罕美国绿卡",
        "转卖排卵监测仪"
    ]
    for sentence in testCases:
        print(HanLP.segment(sentence))
    # 关键词提取
    document = ["水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
                "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
                "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
                "严格地进行水资源论证和取水许可的批准。",
                "90后天才少年曹原，世界难题我都攻克了，还会稀罕美国绿卡",
                "转卖排卵监测仪"
                ]
    for doc in document:
        print('关键词提取-Keyword: --> ', HanLP.extractKeyword(doc, 2))
        print('自动摘要-Summary: --> ', HanLP.extractSummary(doc, 3))
        print('短语提取-Phrase: --> ', HanLP.extractPhrase(doc, 3))
    # 自动摘要
    # print(HanLP.extractWords(document, 3))
    # 依存句法分析
    # print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))
    print(HanLP.parseDependency("转卖排卵监测仪"))
