import sys

COIN_NUM = 9
INT_MAX = sys.maxsize
# 최소 3개의 동전
# 번호가 증가하도록 동전 수집
# 동전 수집 안해도 됨
# 같은 위치 중복 가능
n = int(input())
m = 3
a = [ list(input()) for _ in range(n)]

coin_pos = []
selected_pos = []

start_pos = (-1, -1)
end_pos = (-1, -1)

ans = INT_MAX

def dist(a, b):
    (ay, ax), (by, bx) = a, b
    return abs(ay - by) + abs(ax - bx)

def calc():
    num_moves = dist(start_pos, selected_pos[0])
    for i in range(0, m-1):
        num_moves += dist(selected_pos[i], selected_pos[i+1])
    num_moves += dist(selected_pos[m-1], end_pos)
    return num_moves

def find_min(curr_idx, cnt):
    global ans

    if cnt == m:
        ans = min(ans, calc())
        return

    if curr_idx == len(coin_pos):
        return 

    find_min(curr_idx + 1, cnt)

    selected_pos.append(coin_pos[curr_idx])
    find_min(curr_idx + 1, cnt + 1)
    selected_pos.pop()

    




    
for i in range(n):
    for j, elem in enumerate(a[i]):
            if elem == 'S':
                start_pos = (i, j)
            elif elem == 'E':
                end_pos = (i, j)

for num in range(1, COIN_NUM + 1):
    for i in range(n):
        for j in range(n):
            if a[i][j] == str(num):
                coin_pos.append((i, j))


find_min(0, 0)

if ans == INT_MAX:
    ans = -1

print(ans)