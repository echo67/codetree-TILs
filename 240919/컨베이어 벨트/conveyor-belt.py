n, t = tuple(map(int, input().split()))
up = list(map(int, input().split()))
down = list(map(int, input().split()))

def sec_location(n, t):
    for _ in range(t):
        temp_up = up[n-1]
        temp_down = down[n-1]

        for i in range(n-1, 0, -1):
            up[i] = up[i-1]
            down[i] = down[i-1]
            
        up[0] = temp_down
        down[0] = temp_up

sec_location(n, t)

print(*up)
print(*down)