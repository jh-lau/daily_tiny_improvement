"""
  @Author       : liujianhan
  @Date         : 21/3/18 15:29
  @Project      : DailyTinyImprovement
  @FileName     : japronto_demo.py
  @Description  : Placeholder
"""
import codecs
import json
import logging
from datetime import datetime

import yaml
from japronto import Application
from ner.service import inference, load_model

deploy_config = yaml.safe_load(codecs.open('ner/deploy_config.yml'))


def seg_logger(save_file: str) -> None:
    formatter_str = '%(asctime)s %(levelname)-8s %(message)s'
    logging.basicConfig(
        format=formatter_str,
        filename=save_file,
        filemode='w',
        level=logging.INFO
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(formatter_str)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)


def predict(request):
    data = request.json
    logging.info(f"请求的数据为：{data}")
    query = data.get(deploy_config['params'][0])
    type_ = data.get(deploy_config['params'][1])
    has_dic = data.get(deploy_config['params'][2])
    corpus = data.get(deploy_config['params'][3])
    gran = data.get(deploy_config['params'][4])
    hdfs_path = data.get(deploy_config['params'][5])
    result = inference(query, type_, has_dic, corpus, gran, hdfs_path)

    return request.Response(json={'result': result})


app = Application()
r = app.router
r.add_route(deploy_config['url'], predict, 'POST')

if __name__ == '__main__':
    load_model()
    now = deploy_config['logger_file'] if deploy_config['logger_file'] else datetime.now().strftime('%Y%m%d%H%M')
    seg_logger(f'nlp_server_{now}_{deploy_config["port"]}.log')
    app.run(port=deploy_config['port'])
