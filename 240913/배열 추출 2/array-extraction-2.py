import heapq

n = int(input())
pq = []

for _ in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(pq, (num, 1))
    elif num < 0:
        heapq.heappush(pq, (-num, -1))
    else:
        if pq:
            x, sign = heapq.heappop(pq)
            if sign == 1:
                print(x)
            else:
                print(-x)
        else:
            print(0)