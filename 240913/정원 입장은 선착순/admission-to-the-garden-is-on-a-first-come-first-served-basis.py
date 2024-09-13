# 5
# 25 3
# 105 30
# 20 50
# 10 17
# 100 10


A_MAX = 10**9

import heapq
n = int(input())

people = []
for i in range(n):
    a, t = tuple(map(int, input().split()))
    people.append((a, i+1, t))

people.append((A_MAX, n+1, 0))
people.sort()

max_waiting = 0
pq = []

exit_time = 0
for a, num, t in people:
    while a > exit_time and pq:
        _, next_a, next_t = heapq.heappop(pq)
        max_waiting = max(max_waiting, exit_time - next_a)
        exit_time += next_t

    if a > exit_time:
        exit_time = a + t
    
    else:
        heapq.heappush(pq, (num, a, t))

print(max_waiting)