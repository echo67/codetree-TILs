import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []

ans = 0
sum_val = arr[-1]
heapq.heappush(pq, arr[-1])

for k in range(n-2, 0, -1):
    heapq.heappush(pq, arr[k])
    sum_val += arr[k]
    min_val = pq[0]
    avg = (sum_val - min_val)/(n- k -1)
    if avg > ans :
        ans = avg
    
print(f"{ans:.2f}")