"""
  @Author       : liujianhan
  @Date         : 21/1/17 22:32
  @Project      : DailyTinyImprovement
  @FileName     : demo_proto.py
  @Description  : Placeholder
"""
import demo_person_pb2 as pb


def set_info(info_obj):
    info_obj.id = 1
    person = info_obj.people
    person.age = 88
    person.name = 'first_name'
    score1 = person.score.add()
    score1.object = 'python'
    score1.score = 90
    score2 = person.score.add()
    score2.object = 'cpp'
    score2.score = 99
    phone = person.number
    phone.phone = 10023
    phone.type = 2
    return info_obj


if __name__ == '__main__':
    first_info = pb.one()
    one_info = set_info(first_info)
    print(one_info)
