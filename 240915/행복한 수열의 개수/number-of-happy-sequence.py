n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

same = 0
max_same = 1
ans = 0
for i in range(n):
    max_same = 1
    same = 1
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            same +=1
        else:
            same = 1
        max_same = max(same, max_same)
        
    if  max_same >= m:
        ans += 1

for j in range(n):
    max_same = 1
    same = 1
    for i in range(n-1):
        if arr[i][j] == arr[i+1][j]:
            same +=1
        else:
            same = 1
        max_same = max(same, max_same)
    if max_same >= m:
        ans += 1

print(ans)