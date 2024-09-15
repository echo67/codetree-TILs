n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

same = 0
ans = 0
for i in range(n):
    same = 0
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            same +=1
            if same + 1 >= m:
                ans += 1
        else:
            same = 0

for j in range(n):
    same = 0
    for i in range(n-1):
        if arr[i][j] == arr[i+1][j]:
            same +=1
            if same + 1 >= m:
                ans += 1
        else:
            same = 0

print(ans)