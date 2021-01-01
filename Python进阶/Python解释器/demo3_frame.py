"""
  @Author       : liujianhan
  @Date         : 2020/10/9 16:49
  @Project      : DailyTinyImprovement
  @FileName     : demo3_frame.py
  @Description  : 帧在代码执行时被动态地创建与销毁，每一个帧的创建对应一次函数调用，所以每一个帧都有一个 code object 与其关联，
  同时一个 code object 可以拥有多个帧，因为一个函数可以递归调用自己多次。
  解释器用到的另外两个栈，数据栈，执行字节码操作时使用的栈。还有一个叫作块栈，用于特定的控制流，
  比如循环与异常处理。每一个帧都拥有自己的数据栈与块栈。
"""
