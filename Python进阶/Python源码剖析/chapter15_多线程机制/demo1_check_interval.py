"""
  @Author       : liujianhan
  @Date         : 20/10/4 23:46
  @Project      : DailyTinyImprovement
  @FileName     : demo1_check_interval.py
  @Description  :
  线程调度的两个问题：
  1.何时挂起当前线程 --> 执行一定指令后中断检查
  2.如何选择众多等待中的线程进行激活 --> 未知，交给操作系统决定，python本身不干涉
"""
import sys

if __name__ == '__main__':
    print(f"执行 {sys.getcheckinterval()} 指令后启动线程调度机制。")
    sys.setcheckinterval(120)
    print(f"修改后：执行 {sys.getcheckinterval()} 指令后启动线程调度机制。")
