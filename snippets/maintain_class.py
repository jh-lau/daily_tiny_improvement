"""
  @Author       : liujianhan
  @Date         : 20/8/19 22:49
  @Project      : DailyTinyImprovement
  @FileName     : maintain_class.py
  @Description  : 尽量用辅助类维护程序状态，而不是用字典和元组
"""
from collections import defaultdict


class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        by_subject[subject].append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


if __name__ == '__main__':
    book = SimpleGradebook()
    book.add_student('joey')
    book.report_grade('joey', 'math', 90)
    book.report_grade('joey', 'math', 100)
    book.report_grade('joey', 'gym', 100)
    book.report_grade('joey', 'math', 100)
    print(book.average_grade('joey'))