"""
  @Author       : liujianhan
  @Date         : 20/9/30 23:43
  @Project      : DailyTinyImprovement
  @FileName     : demo1_simulator.py
  @Description  :
"""
from typing import Tuple, Dict, List


class Interpreter:
    def __init__(self):
        self.stack = []
        self.env = {}

    def STORE_NAME(self, name):
        if self.stack:
            self.env[name] = self.stack.pop()

    def LOAD_NAME(self, name):
        value = self.env.get(name, '')
        if value:
            self.stack.append(value)

    def LOAD_VALUE(self, number: int):
        self.stack.append(number)

    def ADD_TWO_VALUES(self):
        first = self.stack.pop()
        second = self.stack.pop()
        self.stack.append(sum([first, second]))

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def parse_args(self, instruction, argument, what_to_execute):
        arg = []
        numbers = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']
        if instruction in numbers:
            arg = what_to_execute['numbers'][argument]
        if instruction in names:
            arg = what_to_execute['names'][argument]

        return arg

    def run_code(self, what_to_execute):
        instructions = what_to_execute.get('instructions', [])
        for instruction, argument in instructions:
            args = self.parse_args(instruction, argument, what_to_execute)
            method = getattr(self, instruction)
            if argument is None:
                method()
            else:
                method(args)


if __name__ == '__main__':
    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),  # 第一个数
                         ("LOAD_VALUE", 1),  # 第二个数
                         ("ADD_TWO_VALUES", None),
                         ("LOAD_VALUE", 2),  # 第二个数
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [7, 5, 4]}
    what_to_execute2 = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names": ["a", "b"]}

    interpreter = Interpreter()
    interpreter.run_code(what_to_execute)
    interpreter.run_code(what_to_execute2)
