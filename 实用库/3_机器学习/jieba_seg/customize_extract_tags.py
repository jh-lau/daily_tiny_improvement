"""
  @Author       : liujianhan
  @Date         : 2021/9/1 15:34
  @Project      : DailyTinyImprovement
  @FileName     : customize_extract_tags.py
  @Description  : Placeholder
"""
from operator import itemgetter

from jieba.analyse.tfidf import TFIDF


class CustomizeTFIDF(TFIDF):
    def extract_tags(self, sentence, topK=20, withWeight=False, allowPOS=(), withFlag=False):
        if allowPOS:
            allowPOS = frozenset(allowPOS)
            words = self.postokenizer.cut(sentence)
        else:
            words = self.tokenizer.cut(sentence)
        if isinstance(sentence, list) and not (withFlag and allowPOS and withFlag):
            words = sentence
        freq = {}
        for w in words:
            if allowPOS:
                if w.flag not in allowPOS:
                    continue
                elif not withFlag:
                    w = w.word
            wc = w.word if allowPOS and withFlag else w
            if len(wc.strip()) < 2 or wc.lower() in self.stop_words:
                continue
            freq[w] = freq.get(w, 0.0) + 1.0
        total = sum(freq.values())
        for k in freq:
            kw = k.word if allowPOS and withFlag else k
            freq[k] *= self.idf_freq.get(kw, self.median_idf) / total

        if withWeight:
            tags = sorted(freq.items(), key=itemgetter(1), reverse=True)
        else:
            tags = sorted(freq, key=freq.__getitem__, reverse=True)
        if topK:
            return tags[:topK]
        else:
            return tags


if __name__ == '__main__':
    tfidf = CustomizeTFIDF()
    test_list = ['前男友', '灰姑娘', '躲开', '总裁', '妈妈', '同意', '离开', '孩子', '决定', '为了']
    print(tfidf.extract_tags(test_list))
    print(tfidf.extract_tags(test_list[::-1]))
