"""
  @Author       : Liujianhan
  @Date         : 20/3/22 22:47
  @FileName     : grammar_tree.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import random

grammar_tree = {
    'simple_sentence': 'subject* predicate* object*',
    'subject*': 'attribute* subject',
    'attribute*': 'attribute | null',
    'predicate*': 'adverbial* predicate complement*',
    'adverbial*': 'adverbial | null',
    'complement*': 'complement | null',
    'object*': 'attribute* object',
    'subject': '李大锤 | 梅艳芳 | 刘德华',
    'predicate': '涉嫌 | 不构成 | 诈骗',
    'object': '行为主义 | 集资诈骗罪 | 自首行为',
    'attribute': '令人发指的 | 漂亮的 | 聪明的',
    'adverbial': '从容地 | 狡猾地 | 阴险地',
    'complement': '极了 | 死了 | 得很 | 多了'
}


def generate_sentence_from_template(gram_tree, target):
    if target not in gram_tree:
        return target
    expanded = [generate_sentence_from_template(gram_tree, s)
                for s in random.choice(gram_tree[target].split())]
    return ''.join([e for e in expanded if e != 'null'])


if __name__ == '__main__':
    pass
