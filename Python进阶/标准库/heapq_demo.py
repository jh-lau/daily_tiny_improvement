"""
  @Author       : Liujianhan
  @Date         : 20/8/10 22:51
  @FileName     : heapq_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import heapq

if __name__ == '__main__':
    s = []
    heapq.heappush(s, 5)
    heapq.heappush(s, 3)
    heapq.heappush(s, 7)
    heapq.heappush(s, 4)
    # 元素总是会被按照从高（数值小的树优先级高）到低的顺序从堆中被弹出
    print(heapq.heappop(s))
    print(heapq.heappop(s))
    print(heapq.heappop(s))
    print(heapq.heappop(s))