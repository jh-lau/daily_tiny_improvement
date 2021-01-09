"""
  @Author       : liujianhan
  @Date         : 2021/1/6 16:02
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : Placeholder
"""
import json
import logging
import os
import time
from pprint import pprint as print
import random
import numpy as np
import copy

from websocket import create_connection


def get_logger(log_name: str,
               file_level=logging.FATAL,
               console_level=logging.FATAL,
               filemode="w",
               to_screen: bool = True):  # a,追加, w,覆蓋
    dest_dir = os.path.join(os.path.dirname(__file__)) + "/logs"
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)  # 定义要创建的目录

    log_name = 'logs/' + log_name
    logger = logging.getLogger(log_name)
    # 此处设定等级后，后续的handler再设等级只有比此等级高才有效，否则无效，如此处为INFO，后续的DEBUG将无效
    logger.setLevel(file_level)

    formatter = logging.Formatter('%(asctime)s '
                                  '%(levelname)s '
                                  '[%(filename)s:%(lineno)d:%(funcName)s:%(threadName)s] '
                                  ': %(message)s')

    file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), log_name + '.log'), encoding="utf-8",
                                       mode=filemode)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if to_screen:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def generate_random_pos():
    seed = {"id": "1", "type": "warship", "name": "张小北",
            "position": {"x": 50, "y": 50}}
    reds = []
    blues = []
    blue_range = [np.arange(0, 30), np.arange(70, 100)]
    red_range = [np.arange(20, 45), np.arange(68, 80)]
    for i in range(2):
        x = np.random.choice(random.choice(blue_range))
        y = np.random.choice(random.choice(blue_range))
        seed['id'] = i
        seed['position'] = {'x': float(x), 'y': float(y)}
        blues.append(copy.deepcopy(seed))
    for i in range(6):
        x = np.random.choice(random.choice(red_range))
        y = np.random.choice(random.choice(red_range))
        seed['id'] = i+2
        seed['position'] = {'x': float(x), 'y': float(y)}
        reds.append(copy.deepcopy(seed))
    init_data = {"assumpId": "1143", "initData": {"mapType": "islands",
                                                  "mapUnit": 0.3,
                                                  "reds": reds,
                                                  "blues": blues,
                                                  }}

    return init_data


id_ = '8018afbb-14f7-4fbb-9ced-76ec3b8aa623'
def generate_random_pos_init(obj):
    actor_position = []
    blue_range = [np.arange(0, 30), np.arange(70, 100)]
    red_range = [np.arange(20, 45), np.arange(68, 80)]
    for unit in obj['actorSituation']:
        u = unit['actorState']
        range_ = blue_range if u['eCampType'] == 'BLUE' else red_range
        x = np.random.choice(random.choice(range_))
        y = np.random.choice(random.choice(range_))
        actor_position.append(
            {'id': u['id'], 'x': str(x), 'y': str(y)}
        )

    return actor_position


if __name__ == '__main__':
    data1 = generate_random_pos()
    data = [
        {"event": "create",
         "data": data1},
        {"event": "start"},
        {"event": "controls", "data": {"id": "5", "cmd": "c2s_move", "position": {"x": 99, "y": 99}}},
        {"event": "controls", "data": {"id": "3", "cmd": "c2s_move", "position": {"x": 9, "y": 9}}},
        {"event": "controls", "data": {"cmd": "c2s_situation"}},
        {"event": "controls", "data": {"cmd": "c2s_position", "actor_position": [{"id": "8018afbb-14f7-4fbb-9ced-76ec3b8aa623", "x": 3, "y": 3}]}},
        {"event": "join", "data": {"assumpId": "5ff92422a93ce405ec401741", "actorId": "1"}}
    ]
    logger = get_logger('logger1', file_level=logging.INFO, console_level=logging.INFO)
    # logger.info(data1)
    # url = 'ws://192.168.3.101:9903/combat'
    url = 'ws://10.20.20.125:9903/combat'
    sc = create_connection(url)
    # sc2 = create_connection(url)
    init_cmd = {"event": "controls", "data": {"cmd": "c2s_position", "actor_position": []}}
    # while True:
    # sc.send(json.dumps(data[0]))  # create
    sc.send(json.dumps(data[-1]))  # join
    sc.send(json.dumps(data[1]))  # start
    # sc.send(json.dumps(data[-2]))  # init

    # time.sleep(1)
    # sc.send(json.dumps(data[2]))  # move
    # sc.send(json.dumps(data[3]))  # move
    # print(test())
    count = 0
    # init_flag = False
    init_flag = True
    last_time = None
    while True:
        try:
            # sc.send(json.dumps(data[4]))
            recv = json.loads(sc.recv())
            # print(recv)
            recv = recv.get('data', {})
            if recv:
                obj = recv[0].get('object', {})
                if obj:
                    if init_flag:
                        init_flag = False
                        data = generate_random_pos_init(obj)
                        init_cmd['data']['actor_position'] = data
                        sc.send(json.dumps(init_cmd))  # init
                    timestamp = obj['timestamp']
                    if timestamp != last_time:
                        last_time = timestamp
                        for u in obj['actorSituation']:
                            idx = u['actorState']['id']
                            x, y = np.random.choice(np.arange(0, 100), 2)
                            x, y = int(x), int(y)
                            cmd = {"event": "controls", "data": {"id": str(idx), "cmd": "c2s_move",
                                                                 "position": {"x": str(x), "y": str(y)}}}
                            sc.send(json.dumps(cmd))
                            if idx == id_:
                                x_, y_ = u['actorState']['x'], u['actorState']['y']
                                # return x, y
                                logger.info(f"{count} frame: {x_:.3f}, {y_:.3f}")
                        count += 1
                        if count == 10:
                            logger.info(f'{count}: go up ----------------Y轴要变大------------------')
                            cmd = {"event": "controls", "data": {"id": id_, "cmd": "c2s_move", "position": {"x": x, "y": y+2}}}
                            sc.send(json.dumps(cmd))
                        if count == 11:
                            logger.info(f'{count}: go down --------------Y轴要变小------------------------')
                            cmd = {"event": "controls",
                                   "data": {"id": id_, "cmd": "c2s_move", "position": {"x": x, "y": y - 2}}}
                            sc.send(json.dumps(cmd))
                        if count == 13:
                            logger.info(f'{count}: go left --------------X轴要变小------------------------')
                            cmd = {"event": "controls",
                                   "data": {"id": id_, "cmd": "c2s_move", "position": {"x": x-2, "y": y}}}
                            sc.send(json.dumps(cmd))
                        if count == 14:
                            logger.info(f'{count}: go right --------------X轴要变大------------------------')
                            cmd = {"event": "controls",
                                   "data": {"id": id_, "cmd": "c2s_move", "position": {"x": 50, "y": 50}}}
                            sc.send(json.dumps(cmd))
        except Exception as e:
            # print(recv)
            print(f'no data received with error: {e}')
            pass
