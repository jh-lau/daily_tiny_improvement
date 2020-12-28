"""
  @Author       : Liujianhan
  @Date         : 20/8/16 13:08
  @FileName     : rename_file.py
  @ProjectName  : DailyTinyImprovement
  @Description  : 将指定文件夹下的类似01-链表重命名为链表
 """
import os


if __name__ == '__main__':
    dst_path = os.path.abspath('02-算法思想')
    for d in os.listdir(dst_path):
        src = os.path.realpath(os.path.join(dst_path, d))
        temp = d.split('-')[1]
        dst = os.path.realpath(os.path.join(dst_path, temp))
        os.rename(src, dst)