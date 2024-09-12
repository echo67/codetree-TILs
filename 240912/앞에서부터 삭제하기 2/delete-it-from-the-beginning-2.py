import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []

ans = 0
heapq.heappush(pq, arr[-1])
for k in range(n-2, 0, -1):
    heapq.heappush(pq, arr[k])
    
    min_pop = heapq.heappop(pq)
    ans = max(ans, sum(list(pq))/len(pq) )
    heapq.heappush(pq, min_pop)
    


print(f"{ans:.2f}")