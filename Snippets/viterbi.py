"""
  @Author       : Liujianhan
  @Date         : 20/3/15 21:53
  @FileName     : viterbi.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
from typing import List


def viterbi(words: List[str], hmm) -> List[str]:
    """
    Viterbi算法实现。
    :param words: 字符列表
    :param hmm: HMM模型
    :return: 标注过的字符列表
    """
    # unpack the length of words, and number of postags
    N, T = len(words), len(hmm.postags)

    # allocate the decode matrix
    score = [[-float('inf') for j in range(T)] for i in range(N)]
    path = [[-1 for j in range(T)] for i in range(N)]

    for i, word in enumerate(words):
        if i == 0:
            for j, tag in enumerate(hmm.postags):
                score[i][j] = hmm.emit(words, i, tag)
        else:
            for j, tag in enumerate(hmm.postags):
                best, best_t = -1e20, -1
                temp = 0
                # Your code here, enumerate all the previous tag
                for j2, tag2 in enumerate(hmm.postags):
                    if best < hmm.trans(tag2, tag) * score[i - 1][j2]:
                        best = hmm.trans(tag2, tag) * score[i - 1][j2]
                        best_t = j2
                best *= hmm.emit(words, i, tag)
                score[i][j] = best
                path[i][j] = best_t

    #
    best, best_t = -1e20, -1
    for j, tag in enumerate(hmm.postags):
        if best < score[len(words) - 1][j]:
            best = score[len(words) - 1][j]
            best_t = j

    result = [best_t]
    best, best_t = -1e20, -1
    best_t = result[0]
    for i in range(len(words) - 1, 0, -1):
        # Your code here, back trace to recover the full viterbi decode path
        result.append(path[i][best_t])
        best_t = result[-1]  # result[-1]代表的是挑选最后一个

    # convert POStag indexing to POStag str
    result = [hmm.postags[t] for t in reversed(result)]
    return result
