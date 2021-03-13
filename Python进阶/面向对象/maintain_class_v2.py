"""
  @Author       : liujianhan
  @Date         : 20/8/19 22:49
  @Project      : DailyTinyImprovement
  @FileName     : maintain_class.py
  @Description  : 尽量用辅助类维护程序状态，而不是用字典和元组
"""
from collections import defaultdict, namedtuple

Grade = namedtuple("Grade", ('score', 'weight'))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight

        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        self._subjects.setdefault(name, Subject())
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._student = {}

    def student(self, name):
        self._student.setdefault(name, Student())
        return self._student[name]


if __name__ == '__main__':
    book = Gradebook()
    albert = book.student('albert')
    math = albert.subject('math')
    math.report_grade(90, 0.2)
    math.report_grade(70, 0.2)
    print(albert.average_grade())
