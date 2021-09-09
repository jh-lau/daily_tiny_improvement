"""
  @Author       : liujianhan
  @Date         : 2021/8/4 9:37
  @Project      : DailyTinyImprovement
  @FileName     : demo_mtl.py
  @Description  : 借助世界上最大的多语种语料库，HanLP2.1支持包括简繁中英日俄法德在内的104种语言上的10种联合任务：
  分词（粗分、细分2个标准，强制、合并、校正3种词典模式）、词性标注（PKU、863、CTB、UD四套词性规范）、
  命名实体识别（PKU、MSRA、OntoNotes三套规范）、依存句法分析（SD、UD规范）、
  成分句法分析、语义依存分析（SemEval16、DM、PAS、PSD四套规范）、语义角色标注、词干提取、词法语法特征提取、抽象意义表示（AMR）。
  https://hanlp.hankcs.com/docs/data_format.html
  https://hanlp.hankcs.com/docs/annotations/index.html
  tok: 分词
  pos: 词性标注 - https://hanlp.hankcs.com/docs/annotations/pos/ctb.html
  lem：词干提取
  fea：词法语法特征
  ner: 实体识别 - https://hanlp.hankcs.com/docs/annotations/ner/msra.html
  dep: 依存句法分析 - https://hanlp.hankcs.com/docs/annotations/dep/sd_zh.html
  con: 短语成分分析 - https://hanlp.hankcs.com/docs/annotations/constituency/ctb.html
  srl: 语义角色标注 - https://hanlp.hankcs.com/docs/annotations/srl/cpb.html
  sdp: 语义依存分析 - https://hanlp.hankcs.com/docs/annotations/sdp/semeval16.html -> 事件抽取
  amr：抽象意义表示
"""
import time

import hanlp
from functools import partial


def get_con_np(document):
    filtered_format = {'NP', 'VP', 'VCD', 'UCP', 'NN'}
    temp_res = {(s.label(), ''.join(s.leaves()), len(s.leaves())) for s in document['con'][0].subtrees()}
    result = {phrase for label, phrase, le in temp_res if label in filtered_format
              if len(phrase) > 1 if le < 4}
    return result


if __name__ == '__main__':
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
    s = ['炸油条最忌加酵母，老师傅教你正确配方和做法，蓬松酥脆不僵硬 最近这段时间宅在家里，面粉可是发挥了它重大的作用，平时感觉不出来，但现在这个时期用处还真不少',
         '用面食作为主食，相比于米饭来说可以省掉炒菜的环节，而且用面粉可以做的主食非常多，手擀面、炒面、焖面、凉皮、锅贴、烙饼、发面饼等等，一种面粉差不多可以做出上百种的花样',
         '前几天，凉皮在网上特别火，很多人在家闲不住都会自己做凉皮吃，做成功的不少，当然失败的也挺多', '最近这几天，炸油条也比较热门，全民都在炸油条，很长时间没吃油条了，小编也忍不住炸了一锅',
         '说到炸油条，可是小编比较拿手的面食',
         '小编的炸油条做法是和一位从事面点工作几十年的老师傅学来的，老师傅说，老一辈的炸油条用的是盐、碱、矾，炸出来的油条蓬松度和酥脆度都非常好，但现在市面上已经禁止食用明矾，现在油条店里大多数炸油条的配方都是盐、小苏打、泡打粉，只要掌握好三者之间的比例和和面技巧、手法，在家也一样可以做出蓬松酥脆的油条',
         '小编发现不少人在炸油条的时候都会放酵母粉，用酵母粉炸过油条的朋友肯定也不难发现，油条的蓬松度不是特别好，而且放凉了以后特别僵硬',
         '话不多说，下面小编就为大家分享炸油条的详细比例和做法，喜欢的朋友可以收藏起来，有时间学着做，包你做的和外面卖的一样好吃',
         '---【炸油条】--- 准备食材：面粉500克、泡打粉10克、小苏打5克、盐5克、食用油20克、清水270克', '做法步骤： 1、把500克面粉放在盆中，加入10克泡打粉、5克小苏打、5克盐、用筷子搅拌均匀',
         '2、把20克食用油倒入面粉中搅拌均匀，然后倒入270克左右的清水，把面粉搅拌成面絮后，下手揉成面团，盖上盖子醒面10分钟',
         '炸油条的面要活得稍微软一点，这样炸出来的油条不会发僵发硬，和面的时候加食用油是表皮酥脆的关键', '3、10分钟后再次揉面、踹面，把面团充分揉光、柔滑',
         '4、把揉好的面团按扁后放在盘子中，包上保鲜膜，放入冰箱冷藏保存6小时以上', '5、炸油条之前，要把面团提前1小时从冰箱中取出来，让面团的温度回升到常温状态',
         '6、面团在常温下醒面1小时后，撕掉保鲜膜，把面片放在案板上，用擀面杖擀长', '面团从冰箱取出后，切记不可再进行揉面', '7、把擀开的面片分成6厘米左右宽、0', '5厘米厚的长面片，再切成2厘米左右宽一个的剂子',
         '8、把切好的小剂子，两两叠在一起，用刀背压一下，防止炸油条的过程中，油条散开', '油条胚子不能太细太薄，否则即使油条充分膨胀，内部也不会形成大的孔洞',
         '9、锅里加入食用油，油温烧至六成热左右，把火力转为中火，把做好的油条胚子用两手稍微拉长，下入油锅中',
         '下入油锅中以后，要用筷子不时地翻动，让油条均匀受热，随着翻动，油条也会越来越蓬松，大概炸20秒左右，油条表面会变成诱人的金黄色，捞出控油即可',
         '10、依次把所有油条炸完，炸好的油条表皮是酥脆的，掰开看，内部都是大孔洞、非常蓬松', '小贴士： 1、和面的时候加油，可以使油条口感酥脆', '2、油条的面要活得稍软一些，这样炸出来的油条不会僵硬',
         '3、炸油条最好不要加酵母粉，加酵母粉炸出来的蓬松度不够好，口感也差些，放凉了还会发硬', '4、醒发好的面团从冰箱中取出后，不能再揉面，直接擀开即可',
         '5、炸油条时的油温要稍高一点，保持一个温度，用筷子不时地翻动，使其均匀受热', '以上就是小编为大家分享的炸油条配方以及技巧，您学会了吗', '关注小酥肉美食，每天为您分享各种美食做法与技巧']
    bad_cases = [

    ]
    model_path = r'C:\Users\MeetYou\AppData\Roaming\hanlp\hanlp\mtl\close_tok_pos_ner_srl_dep_sdp_con_electra_base_20210111_124519'
    # model_path = hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH
    model = hanlp.load(model_path)  # 世界最大中文语料库
    # hanlp.pipeline()
    model['ner/msra'].dict_whitelist = {'花束般恋爱': 'MOVIE', '小水晶': 'PERSON', '1921': 'MOVIE'}
    tok = model['tok/fine']
    tok.dict_force = None
    tok.dict_combine = {'花束般恋爱', '小水晶'}
    t1 = time.time()
    res = []
    # todo: 看为啥同样的文章一次性解析和分条解析的时间差这么多
    for s in sentences + s:
        model(s, tasks='con')
    # result = model([[t] for t in sentences] + s, tasks='con', batch_size=1)
    print(f'{time.time() - t1: .3f}')
    # result.pretty_print()
    # print(result['con'])
