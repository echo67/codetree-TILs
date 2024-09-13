import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []


# prod = 1
# for i in range(n):
#     num = arr[i]
#     if len(pq) < 3 :
#         heapq.heappush(pq, -num)
#         prod *= num
#         print(-1)
#     else:
#         if -pq[0] > num:
#             pop_value = -heapq.heappop(pq)
#             heapq.heappush(pq, -num)
#             prod = int(prod / pop_value * num)
#             print(prod)
#         else:
#             print(prod)
prod = 1
for num in arr:
    heapq.heappush(pq, -num)
    prod *= num

    if len(pq) < 3:
        print(-1)
    else:
        if len(pq) >=4:
            pop_value = -heapq.heappop(pq)
            prod = int(prod / pop_value)
        print(prod)