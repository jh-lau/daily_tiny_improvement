"""
  @Author       : liujianhan
  @Date         : 2021/1/6 16:02
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : Placeholder
"""
import json
import logging
import time
from pprint import pprint as print

from websocket import create_connection

from logger_demo_日志设置 import get_logger



if __name__ == '__main__':
    data = [
        {"event": "create",
         "data": {"assumpId": "1243", "initData": {"mapType": "islands",
                                                   "reds": [{"id": "1", "type": "warship", "name": "张小北",
                                                             "position": {"x": 50, "y": 50}}],
                                                   "blues": [], }
                  }},
        {"event": "start"},
        {"event": "controls", "data": {"id": "1", "cmd": "c2s_move", "position": {"x": 99, "y": 99}}},
        {"event": "controls", "data": {"cmd": "c2s_situation"}},
        {"event": "join", "data": {"assumpId": "1243", "actorId": "1"}}
    ]
    logger = get_logger('logger1', file_level=logging.INFO, console_level=logging.INFO)
    url = 'ws://192.168.3.101:9903/combat'
    # url = 'ws://10.20.20.125:9903/combat'
    # sc = create_connection(url)
    sc2 = create_connection(url)

    # while True:
    # sc.send(json.dumps(data[0]))  # create
    sc2.send(json.dumps(data[-1]))  # join

    # sc.send(json.dumps(data[1]))  # start
    # time.sleep(1)
    # sc.send(json.dumps(data[2]))  # move
    # print(test())
    count = 0
    lx, ly = None, None
    while True:
        try:
            sc2.send(json.dumps(data[3]))
            recv = json.loads(sc2.recv())
            obj = recv.get('object', {})
            if obj:
                for u in recv['object']['actorSituation']:
                    if u['actorState']['id'] == '1':
                        x, y = u['actorState']['x'], u['actorState']['y']
                        # if (x, y) != (lx, ly):
                        #     lx, ly = x, y
                        # return x, y
                        logger.info(f"{x:.3f}, {y:.3f}")
                # count += 1
                # if count == 500:
                #     logger.info(f'{count}: go 0 0')
                #     cmd = {"event": "controls", "data": {"id": "1", "cmd": "c2s_move", "position": {"x": 0, "y": 0}}}
                #     sc.send(json.dumps(cmd))
                #     time.sleep(1)
                # else:
                #     print(f'{count}: go 100 100')
                #     cmd = {"event": "controls", "data": {"id": "1", "cmd": "c2s_move", "position": {"x": 90, "y": 90}}}
                #     sc.send(json.dumps(cmd))
        except Exception as e:
            # print(recv)
            # print(f'no data received with error: {e}')
            pass
