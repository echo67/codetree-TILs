n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

row_visited = [False] * n
col_visited = [False] * n

selected_num = []

ans = 0
def find_max(curr):
    global ans
    if curr == n:
        ans = max(ans, sum(selected_num))
        return

    for i in range(n):
        for j in range(n):
            if row_visited[i] or col_visited[j]:
                continue

            selected_num.append(a[i][j])
            row_visited[i] = True
            col_visited[j] = True

            find_max(curr + 1)

            selected_num.pop()
            row_visited[i] = False
            col_visited[j] = False

find_max(0)
print(ans)