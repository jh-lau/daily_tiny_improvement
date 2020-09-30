"""
  @Author       : liujianhan
  @Date         : 20/9/30 23:43
  @Project      : DailyTinyImprovement
  @FileName     : inter1.py
  @Description  : Placeholder
"""


class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def ADD_TWO_VALUES(self):
        first = self.stack.pop()
        second = self.stack.pop()
        self.stack.append(sum([first, second]))

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def run_code(self, what_to_execute):
        instructions = what_to_execute.get('instructions', [])
        numbers = what_to_execute.get('numbers', [])
        for step in instructions:
            instruction, argument = step
            if instruction == 'LOAD_VALUE':
                value = numbers[argument]
                self.LOAD_VALUE(value)
            if instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            if instruction == 'PRINT_ANSWER':
                self.PRINT_ANSWER()


if __name__ == '__main__':
    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),  # 第一个数
                         ("LOAD_VALUE", 1),  # 第二个数
                         ("ADD_TWO_VALUES", None),
                         ("LOAD_VALUE", 2),  # 第二个数
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [7, 5, 4]}

    interpreter = Interpreter()
    interpreter.run_code(what_to_execute)