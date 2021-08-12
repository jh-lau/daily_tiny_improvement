"""
  @Author       : liujianhan
  @Date         : 2021/8/4 9:37
  @Project      : DailyTinyImprovement
  @FileName     : demo_mtl.py
  @Description  : 借助世界上最大的多语种语料库，HanLP2.1支持包括简繁中英日俄法德在内的104种语言上的10种联合任务：
  分词（粗分、细分2个标准，强制、合并、校正3种词典模式）、词性标注（PKU、863、CTB、UD四套词性规范）、
  命名实体识别（PKU、MSRA、OntoNotes三套规范）、依存句法分析（SD、UD规范）、
  成分句法分析、语义依存分析（SemEval16、DM、PAS、PSD四套规范）、语义角色标注、词干提取、词法语法特征提取、抽象意义表示（AMR）。
  tok: 分词
  pos: 词性标注
  ner: 实体识别
  srl: 语义角色标注
  dep: 依存句法分析
  sdp: 语义依存分析
  con:
"""
import hanlp

if __name__ == '__main__':
    sentences = ["我来到北京清华大学", "乒乓球拍卖完了", "中国科学技术大学", "他来到了网易杭研大厦",
                 '「台中」正确应该不会被切开',
                 '如果放到post中将出错。',
                 "小明硕士毕业于中国科学院计算所，后在日本京都大学深造",
                 '阿婆主来到北京立方庭参观自然语义科技公司。',
                 '华纳音乐旗下的新垣结衣在12月21日于日本武道馆举办歌手出道活动',
                 "90后天才少年曹原，世界难题我都攻克了，还会稀罕美国绿卡",
                 "转卖排卵监测仪"
                 ]
    model_path = r'C:\Users\MeetYou\AppData\Roaming\hanlp\hanlp\mtl\close_tok_pos_ner_srl_dep_sdp_con_electra_base_20210111_124519'
    # model_path = hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH
    HanLP = hanlp.load(model_path)  # 世界最大中文语料库
    for s in sentences:
        r = HanLP([s], tasks='tok/coarse')
        t = HanLP([s], tasks='ner')
        r.pretty_print()
        t.pretty_print()
        tmp = r
