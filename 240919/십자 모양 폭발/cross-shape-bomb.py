n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r-1, c-1
temp = [[0]*n for _ in range(n)]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def bomb_ft(r,c):
    bomb = [[False]*n for _ in range(n)]
    k = arr[r][c]-1
    for i in range(r-k, r+k+1):
        if in_range(i, c):
            bomb[i][c] = True
    for j in range(c-k, c+k+1):
        if in_range(r, j):
            bomb[r][j] = True           
    return bomb

def pull():
    bomb = bomb_ft(r,c)
    for j in range(n):
        temp_idx = n-1
        for i in range(n-1, -1, -1):
            if bomb[i][j] == False:
                temp[temp_idx][j] = arr[i][j] 
                temp_idx = temp_idx - 1

        for i in range(n):
            arr[i][j] = temp[i][j]


pull()
for i in range(n):
    print(*arr[i])