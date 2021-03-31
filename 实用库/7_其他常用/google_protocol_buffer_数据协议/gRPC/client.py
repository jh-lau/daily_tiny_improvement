"""
  @Author       : liujianhan
  @Date         : 2021/1/22 11:34
  @Project      : DailyTinyImprovement
  @FileName     : client.py
  @Description  : Placeholder
"""
import engine_pb2 as e_pb
import engine_pb2_grpc as e_grpc
import grpc


if __name__ == '__main__':
    channel = grpc.insecure_channel('127.0.0.1:2333')
    client = e_grpc.EngineStub(channel=channel)

    create_response = client.create_game(e_pb.RequestCreateGame())
    print(create_response.create_res)
    # join_req = e_pb.RequestJoinGame()
    join_res = client.join_game(e_pb.RequestJoinGame(join_info=['joe', 'lau', 'seeker']))
    print(join_res.join_info)
