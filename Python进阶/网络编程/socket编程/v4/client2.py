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
import random
from pprint import pprint as print

import numpy as np
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


id_ = '8018afbb-14f7-4fbb-9ced-76ec3b8aa623'


def generate_random_pos_init(obj):
    actor_position = []
    blue_range = [np.arange(0, 30), np.arange(70, 100)]
    red_range = [np.arange(20, 45), np.arange(68, 80)]
    for unit in obj['actorSituation']:
        u = unit['actorState']
        if u['actorType'] != 'FACILITY':
            range_ = blue_range if u['eCampType'] == 'BLUE' else red_range
            x = np.random.choice(random.choice(range_))
            y = np.random.choice(random.choice(range_))
            actor_position.append(
                {'id': u['id'], 'x': str(x), 'y': str(y)}
            )

    return actor_position


if __name__ == '__main__':
    raw_data = [
        {"event": "create", "data": {"assumpId": "5ffd12d0a93ce405ec401755", "initData": {"blues": [
            {"id": "b10eecfa-6c95-4172-87e3-3fa704256b7e", "name": "塔里斯曼L",
             "position": {"rotation": 0.0, "x": 104.28572358317545, "y": 61.23018028101585, "z": 0.0},
             "type": "warship", "weapons": {"main": "", "sub": ""}},
            {"id": "e1a81167-db02-49f2-82c9-152f3b3eb2f0", "name": "保护者",
             "position": {"rotation": 0.0, "x": 105.00702253441077, "y": 54.67109424248724, "z": 0.0},
             "type": "warship", "weapons": {"main": "", "sub": ""}}], "cmd": 0, "mapType": "islands", "mapUnit": 0.05,
            "reds": [
                {"id": "6b5830c7-53ef-4827-82f0-76a14ef6d017",
                 "name": "塔里斯曼L",
                 "position": {"rotation": 0.0,
                              "x": 57.621531234801616,
                              "y": 46.12977445911554,
                              "z": 0.0}, "type": "warship",
                 "weapons": {"main": "", "sub": ""}},
                {"id": "a7759e34-13f1-473a-8df4-d1ff350adaca",
                 "name": "指挥所", "position": {"rotation": 0.0,
                                             "x": 63.79353282810333,
                                             "y": 49.87613831883273,
                                             "z": 0.0},
                 "type": "facility",
                 "weapons": {"knife": "", "main": "",
                             "sub": ""}},
                {"id": "06f7422c-9a51-4541-80e1-7d4f79b4be3e",
                 "name": "突击者", "position": {"rotation": 0.0,
                                             "x": 74.31288529725954,
                                             "y": 48.423688698797164,
                                             "z": 0.0},
                 "type": "warship",
                 "weapons": {"main": "", "sub": ""}},
                {"id": "a627b63b-79ca-4979-9127-376598798602",
                 "name": "探索者", "position": {"rotation": 0.0,
                                             "x": 67.90370719039164,
                                             "y": 52.60581563634765,
                                             "z": 0.0},
                 "type": "warship",
                 "weapons": {"main": "", "sub": ""}},
                {"id": "6b0bfc61-c3b3-4d56-8303-f36b05512b7c",
                 "name": "探索者", "position": {"rotation": 0.0,
                                             "x": 59.862625559949336,
                                             "y": 52.54856342848452,
                                             "z": 0.0},
                 "type": "warship",
                 "weapons": {"main": "", "sub": ""}},
                {"id": "b130c1e0-4675-4ead-9bd2-e7fe405d1e86",
                 "name": "斯巴达", "position": {"rotation": 0.0,
                                             "x": 55.766034592680704,
                                             "y": 51.46057522780729,
                                             "z": 0.0},
                 "type": "warship",
                 "weapons": {"main": "", "sub": ""}},
                {"id": "07bbf37a-013e-4d46-8130-12adc583f0b1",
                 "name": "突击者", "position": {"rotation": 0.0,
                                             "x": 53.45337693007105,
                                             "y": 49.168854268991616,
                                             "z": 0.0},
                 "type": "warship",
                 "weapons": {"main": "", "sub": ""}},
                {"id": "7af9d36d-e885-4caa-829c-f36f21e2e0bd",
                 "name": "指挥所", "position": {"rotation": 0.0,
                                             "x": 64.85278973913228,
                                             "y": 49.58784592354092,
                                             "z": 0.0},
                 "type": "facility",
                 "weapons": {"knife": "", "main": "",
                             "sub": ""}}]}}},
        {"event": "start"},
        {"event": "controls", "data": {"id": "5", "cmd": "c2s_move", "position": {"x": 99, "y": 99}}},
        {"event": "controls", "data": {"id": "3", "cmd": "c2s_move", "position": {"x": 9, "y": 9}}},
        {"event": "controls", "data": {"cmd": "c2s_situation"}},
        {"event": "controls", "data": {"cmd": "c2s_position", "actor_position": [
            {"id": "8018afbb-14f7-4fbb-9ced-76ec3b8aa623", "x": 3, "y": 3}]}},
        {"event": "join", "data": {"assumpId": "5ffd12d0a93ce405ec401755", "actorId": "1"}}
    ]
    logger = get_logger('logger1', file_level=logging.INFO, console_level=logging.INFO)
    # logger.info(data1)
    # url = 'ws://192.168.3.101:9903/combat'
    url = 'ws://10.20.20.125:9903/combat'
    sc = create_connection(url)
    # sc2 = create_connection(url)
    init_cmd = {"event": "controls", "data": {"cmd": "c2s_position", "actor_position": []}}
    restart_cmd = {'event': 'restart'}
    # while True:
    # sc.send(json.dumps(raw_data[0]))  # create
    sc.send(json.dumps(raw_data[-1]))  # join
    sc.send(json.dumps(raw_data[1]))  # start
    # sc.send(json.dumps(data[-1]))  # join
    # sc.send(json.dumps(data[1]))  # start
    # sc.send(json.dumps(data[-2]))  # init

    # time.sleep(1)
    # sc.send(json.dumps(data[2]))  # move
    # sc.send(json.dumps(data[3]))  # move
    # print(test())
    ep_count = 1
    count = 0
    # init_flag = False
    init_flag = True
    last_time = None
    game_over = 0
    while True:
        if game_over:
            sc.send(json.dumps(restart_cmd))
            print(f"游戏重启中。。。")
            game_over = 0
            count = 0
            init_flag = True
            last_time = None
            ep_count += 1
        else:
            recv_raw = json.loads(sc.recv())
            recv = recv_raw.get('data', {})
            if recv:
                # print(recv)
                obj = recv[0].get('object', {})
                if obj:
                    terminated = obj['battleOverType']
                    timestamp = obj['timestamp']
                    if terminated > 0:
                        print(f"当前游戏结束，重启游戏：{terminated}")
                        game_over = terminated
                        for i, u in enumerate(obj['actorSituation']):
                            if u['actorState']['actorType'].upper() == 'WARSHIP':
                                if u['actorState']['eCampType'] == 'BLUE':
                                    print(u['actorState']['id'])
                                    print(u['actorState']['bDeath'])
                    elif timestamp != last_time:
                        last_time = timestamp
                        red = []
                        blue = []
                        for i, u in enumerate(obj['actorSituation']):
                            if u['actorState']['actorType'].upper() == 'WARSHIP':
                                if u['actorState']['eCampType'] == 'BLUE':
                                    blue.append(u)
                                else:
                                    red.append(u)
                        for i, u in enumerate(red):
                            idx = u['actorState']['id']
                            x, y = i * 20, 50
                            cmd = {"event": "controls", "data": {"id": str(idx), "cmd": "c2s_move",
                                                                 "position": {"x": str(x), "y": str(y)}}}
                            sc.send(json.dumps(cmd))
                            if not i:
                                logger.info(f"第 {ep_count} 局游戏：{count} frame: {x:.3f}, {y:.3f}")

                        for i, u in enumerate(blue):
                            idx = u['actorState']['id']
                            x, y = i * 20, 50
                            cmd = {"event": "controls", "data": {"id": str(idx), "cmd": "c2s_move",
                                                                 "position": {"x": str(x), "y": str(y)}}}
                            sc.send(json.dumps(cmd))
                        count += 1
                    if init_flag:
                        init_flag = False
                        data = generate_random_pos_init(obj)
                        init_cmd['data']['actor_position'] = data
                        sc.send(json.dumps(init_cmd))  # init
            else:
                # print(recv_raw)
                pass
