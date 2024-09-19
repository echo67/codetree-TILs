n, m, q = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

def right_shift(row):
    global arr
    temp = arr[row][m-1]
    for i in range(m-1, 0, -1):
        arr[row][i] = arr[row][i-1]
    arr[row][0] = temp

def left_shift(row):
    global arr
    temp = arr[row][0]
    for i in range(0, m-1):
        arr[row][i] = arr[row][i+1]
    arr[row][m-1] = temp

def check_up(row):
    global arr
    check_sum = False
    
    if row == 0:
        return False

    for i in range(m):
        if arr[row][i] == arr[row-1][i]:
            check_sum = True
    return check_sum

def check_down(row):
    global arr
    check_sum = False

    if row == n-1:
        return False

    for i in range(m):
        if arr[row][i] == arr[row+1][i]:
            check_sum = True
    return check_sum

def run():
    global arr
    if d == 'R':
        left_shift(r) 
    elif d == 'L':
        right_shift(r)

    r_up = r
    dir_up = d
    dir_down = d

    while check_up(r_up):
        r_up = r_up-1
        if dir_up == 'R':
            right_shift(r_up)
            dir_up = 'L'
        elif dir_up == 'L':
            left_shift(r_up)
            dir_up = 'R'

    r_down = r
    while check_down(r_down):
        r_down = r_down+1
        if dir_down == 'R':
            right_shift(r_down)
            dir_down = 'L'
        elif dir_down == 'L':
            left_shift(r_down)
            dir_down = 'R'




for _ in range(q):
    r, d = tuple(input().split())
    r = int(r)-1
    run()

for i in range(n):
    print(*arr[i])