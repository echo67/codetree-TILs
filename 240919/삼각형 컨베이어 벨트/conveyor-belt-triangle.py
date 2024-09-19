n, t = tuple(map(int, input().split()))

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

def lotation(n):
    temp = third[n-1]

    for i in range(n-1, 0, -1):
        third[i] = third[i-1]

    third[0] = second[n-1]

    for i in range(n-1, 0, -1):
        second[i] = second[i-1]
    second[0] = first[n-1]

    for i in range(n-1, 0, -1):
        first[i] = first[i-1]

    first[0] = temp

for _ in range(t):
    lotation(n)

print(*first)
print(*second)
print(*third)