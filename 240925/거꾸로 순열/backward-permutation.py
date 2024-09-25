n = int(input())
visited = [False] * (n+1)
ans = []

def print_ans():
    for elem in ans:
        print(elem, end = ' ')
    print()


def find_per(curr):
    if curr == n+1:
        print_ans()
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        else:
            visited[i] = True
            ans.append(i)

            find_per(curr + 1)

            ans.pop()
            visited[i] = False

find_per(1)