"""
  @Author       : liujianhan
  @Date         : 2020/11/27 13:40
  @Project      : DailyTinyImprovement
  @FileName     : roc_auc.py
  @Description  :
"""
from sklearn.metrics import roc_curve, auc


def auc_v1(label, pre):
    pos = []
    neg = []
    for i, l in enumerate(label):
        if l:
            pos.append(i)
        else:
            neg.append(i)
    auc = 0
    for p in pos:
        for n in neg:
            if pre[p] > pre[n]:
                auc += 1
            elif pre[p] == pre[n]:
                auc += .5

    return auc / (len(neg) * len(pos))


# Not right.
def auc_v2(label, pre):
    f = zip(label, pre)
    rank = [v for v, _ in sorted(f, key=lambda x: x[1])]
    rank_list = [i + 1 for i, r in enumerate(rank) if r]
    pos = neg = 0
    for i, l in enumerate(label):
        if l:
            pos += 1
        else:
            neg += 1

    return (sum(rank_list) - (pos * (pos + 1)) / 2) / (pos * neg)


if __name__ == '__main__':
    label = [1, 0, 0, 0, 1, 0, 1, 0]
    pre = [.9, .8, .3, .1, .4, .9, .66, .7]
    fpr, tpr, th = roc_curve(label, pre)
    print(fpr, tpr, th)
    print(auc(fpr, tpr))
    print(auc_v1(label, pre))
    print(auc_v2(label, pre))
    label1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    pre1 = [.9, .8, .7, .7, .7, .7, .7, .7, .9, .8, .76]
    print(auc_v1(label1, pre1))
