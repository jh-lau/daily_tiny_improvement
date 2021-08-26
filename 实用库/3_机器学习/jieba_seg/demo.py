"""
  @Author       : liujianhan
  @Date         : 2021/8/3 15:01
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  : Placeholder
"""
# encoding=utf-8
import jieba
import jieba.analyse
from pyhanlp import *
import jieba.posseg as pseg

CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")
# StandardTokenizer.SEGMENT.enableAllNamedEntityRecognize(True)
# CustomDictionary.add("乒乓球拍")  # 动态增加
# CustomDictionary.add("新垣结衣")  # 动态增加


if __name__ == '__main__':
    jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
    strs = ['翁虹因疫情和丈夫女儿分开14个月，小水晶已亭亭玉立颜值高',
            '一条空调家居裤的制作全过程',
            '小学“入学年龄”将放宽，只按年限不按月份？教育部给准话',
            '谨慎选择高校和专业，提高自己的投档率',
            '孕期快速入睡有方法，大人孩子都舒服，不得不知的小妙招',
            '九九牙上火，母亲说那就排骨炖海带汤，太烫老九第一次吃得想砸碗	',
            '给大家带来一道我家里吃得最多的美食，也是最近的网红美食——【网红蔬菜蒸包】',
            '婆婆住我家帮我带娃，夏季用电高峰电费一直我出，很不是滋味',
            '糖耐顺利过关，开心',
            '亲们，刚做的思维，帮忙看看能否看的出男女宝啊',
            '大夫说我孕酮低'
            ]
    # jieba.suggest_freq('台中', True)
    # jieba.suggest_freq('乒乓球拍', True)
    # jieba.suggest_freq(('中', '将'), True)
    # jieba.add_word('乒乓球拍', 31)
    for str in strs:
        seg_list = jieba.cut(str, use_paddle=True, HMM=False)  # 使用paddle模式
        print([(word, flag) for word, flag in pseg.cut(str, use_paddle=True)])
        print("Paddle Mode: " + '/'.join(list(seg_list)))

        # seg_list = jieba.cut(str, cut_all=True, HMM=False)
        # print("Full Mode: " + "/ ".join(seg_list))  # 全模式
        seg_list = jieba.cut(str, cut_all=False, HMM=False)
        print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
        print(f"keyword tfidf: {jieba.analyse.extract_tags(str, withWeight=True, allowPOS=('n', 'nr', 'nz'))}")
        print(f"keyword textrank: {jieba.analyse.textrank(str)}")
        print()

    # seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    # print(", ".join(seg_list))
    #
    # seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    # print(", ".join(seg_list))
