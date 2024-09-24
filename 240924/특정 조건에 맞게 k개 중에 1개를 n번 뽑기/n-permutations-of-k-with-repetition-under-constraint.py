k, n = tuple(map(int, input().split()))
seq = []

def print_num():
    print(*seq)


def find(cnt):
    if cnt == n:
        print_num()
        return

    for i in range(1, k+1):
        ### ⭐️⭐️⭐️
        if cnt >= 2 and i == seq[-1] and i == seq[-2]:
            continue
        else:
            seq.append(i)
            find(cnt + 1)
            seq.pop()

find(0)