n, r, c = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

visited_num = []

dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]


curr_num = arr[r-1][c-1]
curr_pos = (r-1, c-1)
visited_num.append(arr[r-1][c-1])
larger_num = 0
larger_pos = curr_pos

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

while True:
    y, x = curr_pos
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        # new_num = arr[ny][nx]

        if in_range(ny, nx) and arr[ny][nx] > curr_num:
            larger_num = arr[ny][nx]
            larger_pos = (ny, nx)
            break

    if larger_pos == curr_pos:
        break
    else:
        visited_num.append(larger_num)
        curr_pos = larger_pos
        curr_num = larger_num


print(*visited_num)