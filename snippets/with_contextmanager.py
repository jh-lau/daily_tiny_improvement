"""
  Author: Liujianhan
  Date: 20/1/18 17:11
  FileName: with_contextmanager.py
  ProjectName: DailyTinyImprovement
  Description: 上下文管理器的具体应用场景
 """
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollbakc()
            raise e
