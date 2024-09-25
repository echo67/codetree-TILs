# 마지막에서 1로 갈때가 문제

n = int(input())
a = [ list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
selected = []

ans = 10000*100
def find_min(curr):
    global ans
    if curr == n-1:
        sum_val = a[0][selected[0]-1]
        for i in range(n-2):
            sum_val += a[selected[i]-1][selected[i+1]-1]
        sum_val += a[selected[-1]-1][0]
        ans = min(ans, sum_val)
        return

    for i in range(2, n+1):
        if visited[i-2]:
            continue

        if curr >= 1 and a[selected[-1]-1][i-1]==0:
            continue

        if curr==n-2 and a[i-1][0]==0:
            continue

        if curr == 0 and a[0][i-1]==0:
            continue

        selected.append(i)
        visited[i-2] = True
        
        find_min(curr + 1)
        
        selected.pop()
        visited[i-2] = False


find_min(0)    
print(ans)

# 2 3 4 중에서 선택