n = int(input())

y, x = tuple(map(int, input().split()))
curr_y, curr_x = y-1, x-1

arr = [list(input()) for _ in range(n)]
elapsed_time = 0
curr_dir = 0

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def wall_exists(y, x):
    return in_range(y, x) and arr[y][x] == '#'


def right_wall_check(y, x):
    wall_dir = (move_dir - 1 + 4) % 4
    ny, nx = y+dys[wall_dir], x+dxs[wall_dir]   
    return in_range(ny, nx) and arr[ny][nx] =='#'

def front_wall_check(y, x):
    ny, nx = y+dys[move_dir], x+dxs[move_dir]
    return in_range(ny, nx) and arr[ny][nx] == '#'

# 오른쪽으로 벽 없을 때 시계방향으로 
def no_right_wall():
    global y, x, move_dir
    move_dir = (move_dir - 1 + 4) % 4
    y, x = y + dys[move_dir], x + dxs[move_dir]

def front_wall():
    global y, x, move_dir
    move_dir = (move_dir + 1) % 4

    if front_wall_check(y, x):
        y, x = y + dys[move_dir], x + dxs[move_dir]
    else:
        front_wall()



step_set = set()
while in_range(curr_y, curr_x):
    if (curr_y, curr_x, curr_dir) in step_set:
        elapsed_time = -1
        break
    
    step_set.add((curr_y, curr_x, curr_dir))
    
    dys = [0, 1, 0, -1]
    dxs = [1, 0, -1, 0]

    ny, nx = curr_y + dys[curr_dir], curr_x + dxs[curr_dir]

    if wall_exists(ny, nx):
        curr_dir = (curr_dir - 1 + 4) % 4

    elif not in_range(ny, nx):
        elapsed_time += 1
        curr_y, curr_x = ny, nx

    else:
        ry = ny + dys[(curr_dir + 1)%4]
        rx = nx + dxs[(curr_dir + 1)%4]

        if wall_exists(ry, rx):
            curr_y, curr_x = ny, nx
            elapsed_time += 1
        else:
            curr_y, curr_x = ry, rx
            curr_dir = (curr_dir + 1) % 4
            elapsed_time += 2

print(elapsed_time)