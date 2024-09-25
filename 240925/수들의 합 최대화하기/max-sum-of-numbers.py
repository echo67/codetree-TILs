n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

selected_col = []

ans = 0
def find_max(curr):
    global ans

    if curr == n:
        sum_val = 0
        for i in range(n):
            sum_val += a[i][selected_col[i]]
        ans = max(ans, sum_val)
        return

    for i in range(n):
        if visited[i]:
            continue

        selected_col.append(i)
        visited[i] = True

        find_max(curr + 1)

        selected_col.pop()
        visited[i] = False


find_max(0)
print(ans)