n, m, k = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

stick = [(0, i) for i in range(k-1, k-1+m)]

def can_go():
    for y, x in stick:
        if arr[y+1][x] == 1:
            return False
    return True

while can_go():
    stick = [(y+1, x) for y, x in stick]

for y, x in stick:
    arr[y][x] = 1

for i in range(n):
    print(*arr[i])