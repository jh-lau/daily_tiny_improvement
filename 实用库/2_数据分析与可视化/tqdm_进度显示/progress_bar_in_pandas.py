"""
  @Author       : liujianhan
  @Date         : 2021/7/21 11:25
  @Project      : DailyTinyImprovement
  @FileName     : progress_bar.py
  @Description  : Placeholder
"""
import pandas as pd
import numpy as np
from tqdm import tqdm

if __name__ == '__main__':
    tqdm.pandas()
    df = pd.DataFrame(np.random.randint(0, int(1e8), (10000, 1000)))
    # Now you can use `progress_apply` instead of `apply`
    df.groupby(0).apply(lambda x: x ** 2)
    # df.groupby(0).progress_apply(lambda x: x ** 2)
