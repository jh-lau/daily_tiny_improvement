"""
  @Author       : liujianhan
  @Date         : 2020/7/20 下午2:10
  @Project      : service_deploy
  @FileName     : flask_service.py
  @Description  : Placeholder
"""
from datetime import datetime

import flask
from flask import request, jsonify
import json
import codecs
import logging
from ner.service import load_model, inference
import yaml


app = flask.Flask(__name__)
deploy_config = yaml.safe_load(codecs.open('../deploy_config.yml'))


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


@app.route(deploy_config['url'], methods=['POST', 'GET'])
def predict():
    data = request.get_data()
    data = json.loads(data)
    logging.info(f"请求的数据为：{data}")
    query = data.get(deploy_config['params'][0])
    type_ = data.get(deploy_config['params'][1])
    has_dic = data.get(deploy_config['params'][2])
    corpus = data.get(deploy_config['params'][3])
    gran = data.get(deploy_config['params'][4])
    hdfs_path = data.get(deploy_config['params'][5])
    result = inference(query, type_, has_dic, corpus, gran, hdfs_path)
    return jsonify({'result': result})


if __name__ == '__main__':
    load_model()
    now = deploy_config['logger_file'] if deploy_config['logger_file'] else datetime.now().strftime('%Y%m%d%H%M')
    seg_logger(f'nlp_server_{now}_{deploy_config["port"]}.log')
    app.run(host='0.0.0.0', port=deploy_config["port"])
