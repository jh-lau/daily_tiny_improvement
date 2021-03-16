"""
  @Author       : liujianhan
  @Date         : 2021/1/21 17:13
  @Project      : DailyTinyImprovement
  @FileName     : sub_class_fetcher.py
  @Description  : Placeholder
"""


class A:
    @classmethod
    def all_subclasses(cls):
        for s in cls.__subclasses__():
            yield s
            for c in s.all_subclasses():
                yield c

    @classmethod
    def name(cls):
        return cls.__name__

    @classmethod
    def priority(cls):
        return None


class B(A):
    @classmethod
    def priority(cls):
        return 1


class C(B):
    @classmethod
    def priority(cls):
        return 2


if __name__ == '__main__':
    print([s.name() for s in A.all_subclasses() if s.priority() > 0])
