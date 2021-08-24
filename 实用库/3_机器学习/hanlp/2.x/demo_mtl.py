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
  sdp: 语义依存分析 - https://hanlp.hankcs.com/docs/annotations/sdp/semeval16.html
  amr：抽象意义表示
"""
import hanlp

if __name__ == '__main__':
    sentences = [
        # '提高自己的投档率',k
        #              '身体缺少一些微量元素而导致孩子挑食厌食',
        '花束般恋爱这部电影还挺文艺的',
        '最近总是咳嗽，不知道是不是感冒了',
    ]
    model_path = r'C:\Users\MeetYou\AppData\Roaming\hanlp\hanlp\mtl\close_tok_pos_ner_srl_dep_sdp_con_electra_base_20210111_124519'
    # model_path = hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH
    HanLP = hanlp.load(model_path)  # 世界最大中文语料库
    for s in sentences:
        # r = HanLP([s], tasks='tok/coarse')
        r = HanLP([s])
        # t = HanLP([s], tasks='ner')
        # r.pretty_print()
        # t.pretty_print()
        # tmp = r
        r.pretty_print()
