"""
  @Author       : liujianhan
  @Date         : 21/1/1 19:01
  @Project      : DailyTinyImprovement
  @FileName     : 中介者模式.py
  @Description  :
"""


class ChatRoom:
    @staticmethod
    def show_message(user, msg):
        print(f'{user.name} 说： {msg}')


class User:
    def __init__(self, name):
        self.name = name

    def send_msg(self, msg):
        ChatRoom.show_message(self, msg)


if __name__ == '__main__':
    user1 = User('小明')
    user2 = User('小红')
    user1.send_msg('早上好')
    user2.send_msg('晚上好')
