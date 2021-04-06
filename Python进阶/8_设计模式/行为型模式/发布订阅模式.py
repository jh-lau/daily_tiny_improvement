"""
  @Author       : liujianhan
  @Date         : 21/1/1 19:01
  @Project      : DailyTinyImprovement
  @FileName     : 发布订阅模式.py
  @Description  : Placeholder
"""


class Event:
    def __init__(self):
        self.client_list = {}

    def listen(self, key, fn):
        if key not in self.client_list:
            self.client_list[key] = []
        self.client_list[key].append(fn)

    def trigger(self, *args, **kwargs):
        fns = self.client_list[args[0]]

        length = len(fns)
        if not fns or length == 0:
            return False

        for fn in fns:
            fn(*args[1:], **kwargs)

        return False

    def remove(self, key, fn):
        if key not in self.client_list or not fn:
            return False

        fns = self.client_list[key]
        length = len(fns)

        for _fn in fns:
            if _fn == fn:
                fns.remove(_fn)

        return True


# 借助继承为对象安装 发布-订阅 功能
class SalesOffice(Event):
    def __init__(self):
        super().__init__()


# 根据自己需求定义一个函数：供事件处理完后调用
def handle_event(event_name):
    def _handle_event(*args, **kwargs):
        print("Price is", *args, "at", event_name)

    return _handle_event


if __name__ == "__main__":
    # 创建2个回调函数
    fn1 = handle_event("event01")
    fn2 = handle_event("event02")

    sales_office = SalesOffice()

    # 订阅event01 和 event02 这2个事件，并且绑定相关的 完成后的函数
    sales_office.listen("event01", fn1)
    sales_office.listen("event02", fn2)

    # 当两个事件完成时候，触发前几行绑定的相关函数
    sales_office.trigger("event01", 1000)
    sales_office.trigger("event02", 2000)

    sales_office.remove("event01", fn1)

    # 打印：False
    print(sales_office.trigger("event01", 1000))
