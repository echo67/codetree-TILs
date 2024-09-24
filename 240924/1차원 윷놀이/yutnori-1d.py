n, m, k = tuple(map(int, input().split()))
given_num = list(map(int, input().split()))
ans = 0
scores = [1 for _ in range(k)] ## 1번 지점부터 시작

def calc():
    score = 0
    for piece in scores:
        if piece >= m:
            score += 1
            # print(scores, ans)
    # scores = [0 for _ in range(n+1)]
    return score

def find(cnt):
    global ans
    ans = max(ans, calc())

    if cnt == n:
        # print(selected_num, scores) 
        return

    for i in range(k):
        if scores[i] >= m:
            continue
        scores[i] += given_num[cnt] ### ⭐️
        find(cnt + 1)
        scores[i] -= given_num[cnt] ### ⭐️ 

find(0)
print(ans)