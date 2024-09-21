n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

# 오른쪽부터 시계방향
dys = [0, 1, 1, 1, 0, -1, -1, -1]
dxs = [1, 1, 0, -1, -1, -1, 0, 1]
move_dir = 0

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

for _ in range(m):
    for k in range(1, n*n+1):
        visited = [False] * (n*n)
        for i in range(n):
            for j in range(n):
                if arr[i][j] == k and visited[k-1] == False:
                    max_val = 0
                    for dy, dx in zip(dys, dxs):
                        ny, nx = i + dy, j + dx
                        if in_range(ny, nx) and arr[ny][nx] > max_val:
                            max_val = arr[ny][nx]
                            max_y, max_x = (ny, nx)
                    arr[i][j] = max_val
                    arr[max_y][max_x] = k
                    visited[k-1] = True

for i in range(n):
    print(*arr[i])