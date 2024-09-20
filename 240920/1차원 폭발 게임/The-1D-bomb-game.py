n, m = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]

def bomb_explode(s, e):
    global bomb_blank
    bomb_len = e - s + 1
    if bomb_len >= m:
        for i in range(s, e+1):
            bomb_blank[i]=False

def run():
    global arr, bomb_blank
    len_arr = len(arr)
    bomb_blank = [True] * len_arr
    temp = []
    s = None
    bomb_len = 0

    for i in range(len_arr-1):
        if arr[i] == arr[i+1] and s == None:
            s = i
            if i+1 == len_arr-1:
                e = len_arr-1
                bomb_explode(s,e)

        elif (arr[i] != arr[i+1] or i==n-1) and s != None:
            e = i
            bomb_explode(s,e)
            s = None

    # 하나라도 폭탄 터졌을 때
    if any(i == False for i in bomb_blank):
        temp = [arr[i] for i in range(len_arr) if bomb_blank[i]]
        arr = [elem for elem in temp]
        len_arr = len(arr)
        if len_arr < m:
            return len_arr
    
    # 터질 폭탄이 없을 때 
    if all(i == True for i in bomb_blank):
        len_arr = len(arr)
        return len_arr

len_arr = None   
while len_arr == None:
    len_arr = run()
print(len_arr)

for i in range(len_arr):
    print(arr[i])