def tri(arr, y, x):
    max_sum = 0

    if y + 1 >= n or x + 1 >= n:
        return 0

    sum_tri1 = arr[y][x] + arr[y+1][x] + arr[y][x+1]
    max_sum = max(max_sum, sum_tri1)

    sum_tri2 = arr[y][x] + arr[y][x+1] + arr[y+1][x+1]
    max_sum = max(max_sum, sum_tri2)

    sum_tri3 = arr[y][x+1] + arr[y+1][x] + arr[y+1][x+1]
    max_sum = max(max_sum, sum_tri3)

    sum_tri4 = arr[y][x] + arr[y+1][x] + arr[y+1][x+1]
    max_sum = max(max_sum, sum_tri4)
    return max_sum

def in_line_y(arr, y, x):
    return y + 2 < n and y + 1 < n 

def in_line_x(arr, y, x):
    return x + 2 < n and x + 1 < n

def line(arr, y, x):
    max_sum = 0
    if in_line_y(arr, y, x):
        sum_tri1 = arr[y][x] + arr[y+1][x] + arr[y+2][x]
        max_sum = max(max_sum, sum_tri1)

        
    return max_sum

def line2(arr, y, x):
    max_sum = 0
    if in_line_x(arr, y, x):
        sum_tri2 = arr[y][x] + arr[y][x+1] + arr[y][x+2]
        max_sum = max(max_sum, sum_tri2)
    return max_sum


n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

max_max = 0
for i in range(n):
    for j in range(m):
        max1 = tri(arr, i, j)
        max2 = line(arr, i, j)
        max3 = line2(arr, i, j)
        max_max = max(max1, max2, max3, max_max)
    

print(max_max)