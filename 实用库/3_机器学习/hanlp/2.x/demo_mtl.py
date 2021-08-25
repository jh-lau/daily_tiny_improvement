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
  ner: 实体识别
  dep: 依存句法分析 - https://hanlp.hankcs.com/docs/annotations/dep/sd_zh.html
  con: 短语成分分析 - https://hanlp.hankcs.com/docs/annotations/constituency/ctb.html
  srl: 语义角色标注 - https://hanlp.hankcs.com/docs/annotations/srl/cpb.html
  sdp: 语义依存分析 - https://hanlp.hankcs.com/docs/annotations/sdp/semeval16.html -> 事件抽取
  amr：抽象意义表示
"""
import time

import hanlp
from hanlp.components.mtl.multi_task_learning import MultiTaskLearning
from hanlp.components.mtl.tasks.tok.tag_tok import TaggingTokenization


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
    # for s in sentences:
    #     # r = model([s], tasks='tok/coarse')
    #     # r = model([s], batch_size=128, tasks=['tok/fine', 'dep', 'ner/msra', 'con'])  # accelerate on gpu
    #     r = model([s], tasks=['ner/msra','con'])  # accelerate on gpu
    #     res.append(r)
    #     # t = model([s], tasks='ner')
    #     # r.pretty_print()
    #     # t.pretty_print()
    #     # tmp = r
    #     r.pretty_print()
    model(sentences, tasks=['con'])
    print(f'{time.time() - t1: .3f}')
