"""
  @Author       : liujianhan
  @Date         : 21/1/1 18:37
  @Project      : DailyTinyImprovement
  @FileName     : 组合模式.py
  @Description  : Placeholder
"""


# Component：公司抽象类
class Company:
    name = ''

    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        pass

    def line_of_duty(self):  # 履行职责
        pass

    # Composite：公司类


class ConcreteCompany(Company):
    childrenCompany = None

    def __init__(self, name):
        Company.__init__(self, name)
        self.childrenCompany = []

    def add(self, company):
        self.childrenCompany.append(company)

    def remove(self, company):
        self.childrenCompany.remove(company)

    def display(self, depth):
        print('-' * depth + self.name)

        for component in self.childrenCompany:
            component.display(depth + 2)

    def line_of_duty(self):  # 履行职责
        for component in self.childrenCompany:
            component.line_of_duty()


# Leaf：具体职能部门
class HRDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print('-' * depth + self.name)

    def line_of_duty(self):  # 履行职责
        print('%s\t员工招聘培训管理' % self.name)


# Leaf：具体职能部门
class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print('-' * depth + self.name)

    def line_of_duty(self):  # 履行职责
        print('%s\t公司财务收支管理' % self.name)


if __name__ == '__main__':
    root = ConcreteCompany('北京总公司')
    root.add(HRDepartment('总公司人力资源部'))
    root.add(FinanceDepartment('总公司财务部'))

    comp = ConcreteCompany('华东分公司')
    comp.add(HRDepartment('华东分公司人力资源部'))
    comp.add(FinanceDepartment('华东分公司财务部'))
    root.add(comp)

    comp1 = ConcreteCompany('南京办事处')
    comp1.add(HRDepartment('南京办事处人力资源部'))
    comp1.add(FinanceDepartment('南京办事处财务部'))
    comp.add(comp1)

    comp2 = ConcreteCompany('杭州办事处')
    comp2.add(HRDepartment('杭州办事处人力资源部'))
    comp2.add(FinanceDepartment('杭州办事处财务部'))
    comp.add(comp2)

    print('-------公司结构图-------')
    root.display(1)

    print('\n-------职责-------')
    root.line_of_duty()
