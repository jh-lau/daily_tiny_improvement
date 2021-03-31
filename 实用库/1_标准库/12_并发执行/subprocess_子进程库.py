"""
  @Author       : liujianhan
  @Date         : 2021/1/27 14:56
  @Project      : DailyTinyImprovement
  @FileName     : subprocess_子进程库.py
  @Description  : Placeholder
"""
from subprocess import Popen, PIPE, STDOUT

if __name__ == '__main__':
    create_proc = 'python zip_demo.py'
    # create_proc = 'dir'
    sub = Popen(create_proc, shell=True, encoding='utf8',
                # cwd=os.path.dirname(__file__),
                # cwd=os.path.dirname(r'C:\Users\dataexa\Desktop\projects\marl\nashzero\701\engine_control'),
                stdout=PIPE,
                stderr=STDOUT
                )
    ret = sub.poll()
    if ret is None:
        res = sub.communicate()[0]
        print(res + '123')
    else:
        print('done')
        print(ret)
    print('outside done')
