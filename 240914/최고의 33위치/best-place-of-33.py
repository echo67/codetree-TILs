n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


max_sum = 0
for i in range(n-2):
    for j in range(n-2):
        sum_v = 0
        for k in range(i, i+3):
            for l in range(j, j+3):
                sum_v += arr[k][l]
        max_sum = max(max_sum, sum_v)
print(max_sum)