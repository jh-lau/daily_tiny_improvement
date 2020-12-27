"""
  @Author       : liujianhan
  @Date         : 20/12/27 21:03
  @Project      : DailyTinyImprovement
  @FileName     : rpyc_demo.py
  @Description  : Placeholder
"""
import rpyc


class MyService(rpyc.Service):
    def on_connect(self, conn):
        print(f"connection from {conn} is connected")

    def on_disconnect(self, conn):
        print(f"connection {conn} disconnected")

    def exposed_get_answer(self):
        return 42

    def get_question(self):
        return "what's your name?"


if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MyService, port=18861)
    t.start()

