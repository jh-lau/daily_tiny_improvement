"""
  @Author       : liujianhan
  @Date         : 2020/9/25 17:52
  @Project      : DailyTinyImprovement
  @FileName     : chaizi_demo.py
  @Description  : Placeholder
"""
import pickle


class ChaiZi:
    def __init__(self, data_path: str):
        with open(data_path, 'rb') as f:
            self.data = pickle.load(f)

    def query(self, input_char, default=None):
        _result = self.data.get(input_char, default)
        return _result


if __name__ == '__main__':
    chaizi = ChaiZi('data.pkl')
    sentence = '我是一个小学生，你敢打我嘛？'
    final = ''
    for char in sentence:
        result = chaizi.query(char)
        if result:
            temp = ''.join(result[0])
            final += temp

    print(final)