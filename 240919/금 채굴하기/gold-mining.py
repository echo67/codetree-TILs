n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
OUT_OF_MARGIN = None

def margin(x, dx, y, dy, n):
    if x + dx > n-1:
        nx = OUT_OF_MARGIN
    elif x + dx < 0:
        nx = OUT_OF_MARGIN
    else: 
        nx = x + dx

    if y + dy > n-1:
        ny = OUT_OF_MARGIN
    elif y + dy < 0:
        ny = OUT_OF_MARGIN
    else: 
        ny = y + dy
    return (ny, nx)


def square(y, x, k):
    gold = 0
    for dy in range(-k, k+1):
        if dy <= 0:
            for dx in range(-k-dy, dy+k+1):
                ny, nx = margin(x, dx, y, dy, n)
                if ny == OUT_OF_MARGIN or nx == OUT_OF_MARGIN:
                    gold += 0
                else:
                    gold += arr[ny][nx]
        if dy > 0:
            for dx in range(-k+dy, -dy+k+1):
                ny, nx = margin(x, dx, y, dy, n)
                if ny == OUT_OF_MARGIN or nx == OUT_OF_MARGIN:
                    gold += 0
                else:
                    gold += arr[ny][nx]
    profit = gold * m - k*k - (k+1) * (k+1)
    return (gold, profit)

max_profit = 0
max_gold = 0
for y in range(n):
    for x in range(n):
        for k in range(n):
            gold, profit = square(y, x, k)
            if profit >= 0 and gold > max_gold:
                max_gold, profit = gold, profit

print(max_gold)