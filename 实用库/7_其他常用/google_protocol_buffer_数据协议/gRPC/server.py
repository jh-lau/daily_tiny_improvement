"""
  @Author       : liujianhan
  @Date         : 2021/1/22 11:24
  @Project      : DailyTinyImprovement
  @FileName     : server.py
  @Description  :
"""
import random

import engine_pb2 as e_pb
import engine_pb2_grpc as e_grpc
import grpc


class Engine(e_grpc.EngineServicer):
    games = ['sc2', 'dota2', 'lol']

    def create_game(self, request_create_game, context):
        return e_pb.ResponseCreateGame(create_res=random.choice(self.games))

    def join_game(self, request_join_game, context):
        join_info = request_join_game.join_info
        res_info = {}
        for ji in join_info:
            res_info[ji] = f"Joining {random.choice(self.games)}"
        return e_pb.ResponseJoinGame(join_info=res_info)


if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor

    grpc_server = grpc.server(ThreadPoolExecutor(max_workers=3))
    e_grpc.add_EngineServicer_to_server(Engine(), grpc_server)
    grpc_server.add_insecure_port('127.0.0.1:2333')
    grpc_server.start()
    import time

    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        grpc_server.stop(0)
