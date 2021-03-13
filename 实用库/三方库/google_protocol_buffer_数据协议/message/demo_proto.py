"""
  @Author       : liujianhan
  @Date         : 21/1/17 22:32
  @Project      : DailyTinyImprovement
  @FileName     : demo_proto.py
  @Description  : Placeholder
"""
# import demo_person_pb2 as pb
import demo_person_pb3_pb2 as pb


def set_info(info_obj):
    info_obj.id = 1
    person = info_obj.people
    person.age = 88
    person.name = 'joey'

    # repeated属性写法1
    score1 = person.score.add()
    score1.object = 'python'
    score1.score = 90
    score2 = person.score.add()
    score2.object = 'cpp'
    score2.score = 99

    # repeated属性写法2
    person.score.add(object='c#', score=20)

    # repeated属性写法3
    score = pb.Person().Score()
    score.object = 'math'
    score.score = 12
    person.score.append(score)

    # map属性写法1
    person.dict_score['physics'].object = 'physics'
    person.dict_score['physics'].score = 100

    phone = person.number
    phone.phone = 10023
    # phone.type = 2
    return info_obj


if __name__ == '__main__':
    first_info = pb.one()
    one_info = set_info(first_info)
    print(one_info)
    print(pb.MOBILE)
