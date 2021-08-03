"""
  @Author       : liujianhan
  @Date         : 2021/8/3 15:01
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  : Placeholder
"""
# encoding=utf-8
import jieba


if __name__ == '__main__':
    jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
    strs=["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学", "他来到了网易杭研大厦",
          '「台中」正确应该不会被切开',
          '如果放到post中将出错。',
          "小明硕士毕业于中国科学院计算所，后在日本京都大学深造",
          '阿婆主来到北京立方庭参观自然语义科技公司。',
          '华纳音乐旗下的新垣结衣在12月21日于日本武道馆举办歌手出道活动']
    jieba.suggest_freq('台中', True)
    jieba.suggest_freq('乒乓球拍', True)
    jieba.suggest_freq(('中', '将'), True)
    jieba.add_word('乒乓球拍', 31)
    for str in strs:
        seg_list = jieba.cut(str,use_paddle=True, HMM=False)  # 使用paddle模式
        print("Paddle Mode: " + '/'.join(list(seg_list)))

        # seg_list = jieba.cut(str, cut_all=True, HMM=False)
        # print("Full Mode: " + "/ ".join(seg_list))  # 全模式

        seg_list = jieba.cut(str, cut_all=False, HMM=False)
        print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

        print()

    seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))
