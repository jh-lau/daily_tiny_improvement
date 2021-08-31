"""
  @Author       : liujianhan
  @Date         : 21/8/3 19:57
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  :
"""
import time

from pyhanlp import *
CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
NLPTokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")
# StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")
# StandardTokenizer.SEGMENT.enableAllNamedEntityRecognize(True)
CustomDictionary.add("花束般恋爱")  #
CustomDictionary.add("美国绿卡")
NotionalTokenizer = JClass("com.hankcs.hanlp.tokenizer.NotionalTokenizer")
StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")
StandardTokenizer.SEGMENT.enableAllNamedEntityRecognize(True)

if __name__ == '__main__':
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
        print(NLPTokenizer.segment(sentence))
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
    sentences = [
        '一条空调家居裤的制作全过程',
        '鸡翅的家常做法',
        '做女人不容易',
        '小学“入学年龄”将放宽',
        '就业率亮红灯的4大专业，985毕业也很难就业，考生报考要谨慎',
        '孕妈的肚子别乱摸，尤其是这种情况，乱摸可能会发生危险，要小心',
        '萝卜白菜汤美味又营养，健康好吃，美味不贵',
        '孕期快速入睡有方法，大人孩子都舒服，不得不知的小妙招',
        '那么，大龄女性如何备孕可以提高怀孕几率呢',
        '成年母子过度亲密意味着家庭关系的错位，和母子关系的畸形',
        '提高自己的投档率',
        '身体缺少一些微量元素而导致孩子挑食厌食',
        '1921这部电影还挺好看的',
        '花束般恋爱这部电影还挺文艺的',
        '翁虹因疫情和丈夫女儿分开14个月，小水晶已亭亭玉立颜值高',
        "泽田依子是上外日本文化经济学院的外教",
        '九九牙上火，母亲说那就排骨炖海带汤，太烫老九第一次吃得想砸碗	',
        '给大家带来一道我家里吃得最多的美食，也是最近的网红美食——【网红蔬菜蒸包】',
        '婆婆住我家帮我带娃，夏季用电高峰电费一直我出，很不是滋味'
    ]
    t1 = time.time()
    for s in sentences:
        print('nlp tokenizer ', NLPTokenizer.segment(s))
        print('standard tokenizer ', StandardTokenizer.segment(s))
        print('notional tokenizer ', NotionalTokenizer.segment(s))
        print('关键词提取-Keyword: --> ', HanLP.extractKeyword(s, 2))
        print('短语提取-Phrase: --> ', HanLP.extractPhrase(s, 6))  # 基本是几类短语组合，可能需要自定义组合
        print(HanLP.parseDependency(s))
    print(f'{time.time() - t1: .3f}')
    # temp = ''
    # with open('test.txt', encoding='utf8') as src:
    #     temp += ''.join([t.strip() for t in src.readlines()])
    # print('新词发现-Words: --> ', HanLP.extractWords(temp, 10))
    # print('新词发现-Words: --> ', HanLP.extractWords(temp, 10, True))

