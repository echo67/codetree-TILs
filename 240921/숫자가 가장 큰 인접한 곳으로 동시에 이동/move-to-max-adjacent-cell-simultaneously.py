# n: 격자 (2<= n<= 20), m: 구슬
n, m, t = tuple(map(int, input().split()))
# 가장 큰 값
# 우선순위: 상하좌우
dys, dxs = [1, -1, 0, 0], [0, 0, -1, 1]
arr = [list(map(int, input().split())) for _ in range(n)]
curr_pos = [tuple(map(int, input().split())) for _ in range(m)]

count = [[0 for _ in range(n)] for _ in range(n)]
next_count = [[0 for _ in range(n)] for _ in range(n)]
# 격자 벗어나면 안됨
def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

for elem in curr_pos:
    y, x = elem
    count[y-1][x-1]=1

def move_next(y, x):
    max_num = 0
    max_pos = (-1, -1)
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        
        if in_range(ny, nx) and arr[ny][nx] > max_num:
            max_num = arr[ny][nx]
            max_pos = (ny, nx)
    return max_pos


for _ in range(t):
    next_pos = []
    next_count = [[0 for _ in range(n)] for _ in range(n)]

    for elem in curr_pos:
        y, x = elem
        ny, nx = move_next(y-1, x-1)
        next_count[ny][nx] += 1
        next_pos.append((ny+1, nx+1))

    count = next_count

    for i in range(n):
        for j in range(n):
            if next_count[i][j] >=2:
                count[i][j] = 0
                
    curr_pos = next_pos
print(sum([count[i][j] for i in range(n) for j in range(n)] ))