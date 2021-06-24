"""
  @Author       : liujianhan
  @Date         : 2021/6/24 16:36
  @Project      : DailyTinyImprovement
  @FileName     : demo1.py
  @Description  : Placeholder
"""
import yaml


def load_yaml_file(file_path: str):
    return yaml.safe_load(open(file_path, 'r', encoding='utf8'))


if __name__ == '__main__':
    file_path = 'test.yaml'
    print(load_yaml_file(file_path))
