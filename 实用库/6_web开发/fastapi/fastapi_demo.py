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
from pydantic import BaseModel

app = FastAPI()
deploy_config = yaml.safe_load(codecs.open('deploy_config.yml'))

print('hello there')
# load_model()


class Query(BaseModel):
    query: str


@app.post(deploy_config['url'])
@app.get(deploy_config['url'])
def predict(request: Query):
    print(request)
    # query = request.query
    result = f'test result: {request}'
    return {'message': result}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('fastapi_demo:app', host='localhost', port=8000, reload=True, workers=2)
