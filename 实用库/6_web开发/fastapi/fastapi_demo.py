"""
  @Author       : liujianhan
  @Date         : 21/3/18 15:30
  @Project      : DailyTinyImprovement
  @FileName     : fastapi_demo.py
  @Description  : Placeholder
"""
import codecs

import yaml
from fastapi import FastAPI
from ner.service import inference, load_model
from pydantic import BaseModel

app = FastAPI()
deploy_config = yaml.safe_load(codecs.open('deploy_config.yml'))

print('hello there')
load_model()


class Query(BaseModel):
    query: str
    type: str
    has_dic: str = ''
    corpus: str
    gran: str = ''
    hdfs_path: str = ''


@app.post(deploy_config['url'])
@app.get(deploy_config['url'])
def predict(request: Query):
    query = request.query
    type = request.type
    has_dic = request.has_dic
    corpus = request.corpus
    gran = request.gran
    hdfs_path = request.hdfs_path
    result = inference(query, type, has_dic, corpus, gran, hdfs_path)
    return {'message': result}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('fastapi_service:app', host='localhost', port=8000, reload=True, workers=2)
