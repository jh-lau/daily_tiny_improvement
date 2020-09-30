"""
  @Author       : liujianhan
  @Date         : 20/9/30 23:28
  @Project      : DailyTinyImprovement
  @FileName     : getitem_len_demo.py
  @Description  : Placeholder
"""


class Company:
    def __init__(self, employee_list=None):
        if employee_list is None:
            self.employee = []
        else:
            self.employee = employee_list

    def __getitem__(self, item):
        print(f"{item}")
        return self.employee[item]

    def __repr__(self):
        return f"Hello Company"


if __name__ == '__main__':
    s = Company(['joey', 'ross', 'chandler'])
    print(s[1])
    temp = s[:2]
    print(len(temp))
    print(s)