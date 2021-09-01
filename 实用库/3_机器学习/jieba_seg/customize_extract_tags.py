"""
  @Author       : liujianhan
  @Date         : 2021/9/1 15:34
  @Project      : DailyTinyImprovement
  @FileName     : customize_extract_tags.py
  @Description  : Placeholder
"""
from operator import itemgetter
from typing import List

from jieba.analyse.tfidf import TFIDF


class CustomizeTFIDF(TFIDF):
    def sort_tok_by_idf(self, tokens: List, topK=20):
        freq = {}
        for w in tokens:
            if len(w.strip()) < 2 or w.lower() in self.stop_words:
                continue
            freq[w] = freq.get(w, 0.0) + 1.0
        total = sum(freq.values())
        for k in freq:
            freq[k] *= self.idf_freq.get(k, self.median_idf) / total

        tags = sorted(freq, key=freq.__getitem__, reverse=True)
        if topK:
            return tags[:topK]
        else:
            return tags


if __name__ == '__main__':
    tfidf = CustomizeTFIDF()
    test_list = ['前男友', '灰姑娘', '躲开', '总裁', '妈妈', '同意', '离开', '孩子', '决定', '为了']
    print(tfidf.sort_tok_by_idf(test_list))
    print(tfidf.sort_tok_by_idf(test_list[::-1]))
    print(tfidf.sort_tok_by_idf(test_list[::-1], topK=3))
