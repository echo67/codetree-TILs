n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
ans = 0

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def can_go(y, x, prev_num):
    return in_range(y, x) and a[y][x] > prev_num

def move(y, x, cnt):
    global ans

    ans = max(ans, cnt)

    dys = [-1, -1, 0, 1, 1, 1, 0, -1]
    dxs = [0, 1, 1, 1, 0, -1, -1, -1]

    d = move_dir[y][x] - 1 

    for i in range(n):
        ny, nx = y + dys[d]*i, x+dxs[d]*i
        if can_go(ny, nx, a[y][x]):
            move(ny, nx, cnt + 1)



move(r-1, c-1, 0)
print(ans)