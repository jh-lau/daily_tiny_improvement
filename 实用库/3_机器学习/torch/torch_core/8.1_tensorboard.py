"""
  @Author       : liujianhan
  @Date         : 21/4/2 17:06
  @Project      : DailyTinyImprovement
  @FileName     : 8.1_tensorboard.py
  @Description  : Placeholder
"""
import numpy as np
from torch.utils.tensorboard import SummaryWriter

if __name__ == '__main__':
    log_dir = 'tensorboard_log'
    writer = SummaryWriter(log_dir=log_dir, comment='test_tensorboard')
    for x in range(100):
        writer.add_scalar('y=2x', x * 2, x)
        writer.add_scalar('y=pow(2, x)', 2 ** x, x)
        writer.add_scalars('data/scalar_group', {
            'xsinx': x * np.sin(x),
            'xcosx': x * np.cos(x),
            'arctanx': np.arctan(x)
        }, x)
    writer.close()
