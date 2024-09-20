n = int(input())

y, x = tuple(map(int, input().split()))
y, x = y-1, x-1
init_y, init_x = y, x

arr = [list(input()) for _ in range(n)]

dys = [0, -1, 0, 1]
dxs = [1, 0, -1, 0]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n
move_dir = 0

# 오른쪽으로 벽 없을 때 시계방향으로 
def no_right_wall():
    global y, x, move_dir
    move_dir = (move_dir - 1 + 4) % 4
    y, x = y + dys[move_dir], x + dxs[move_dir]

def front_wall():
    global y, x, move_dir
    move_dir = (move_dir + 1) % 4
    y, x = y + dys[move_dir], x + dxs[move_dir]

def right_wall_check():
    wall_dir = (move_dir - 1 + 4) % 4
    ny, nx = y+dys[wall_dir], x+dxs[wall_dir]   
    return in_range(ny, nx) and arr[ny][nx] =='#'

def front_wall_check():
    ny, nx = y+dys[move_dir], x+dxs[move_dir]
    return in_range(ny, nx) and arr[ny][nx] == '#'

step = 0
while in_range(y, x):
    if front_wall_check():
        front_wall()
        step += 1
    elif right_wall_check():
        y, x = y + dys[move_dir], x + dxs[move_dir]
        step += 1
    else:
        no_right_wall()
        step += 1
    if (y, x) == (init_y, init_x):
        step = -1
        break

print(step)