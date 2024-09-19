n = int(input())
arr = []
for _ in range(n):
    elem = int(input())
    arr.append(elem)

def in_blank(idx):
    return s <= idx <= e







for _ in range(2):
    s, e = tuple(map(int, input().split()))
    s, e = s-1, e-1

    tmp_idx = 0
    temp = []
    for i in range(n):
        if not in_blank(i):
            temp.append(arr[i])
    arr = temp
    n = len(temp)


print(n)
for i in range(n):
    print(arr[i])