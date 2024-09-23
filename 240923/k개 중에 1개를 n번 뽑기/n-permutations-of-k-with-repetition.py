k, n = tuple(map(int, input().split()))
selected_nums = []

def print_answer():
    for elem in selected_nums:
        print(elem, end=" ")
    print()

def find_per(cnt):
    if cnt == n:
        print_answer()
        return

    for i in range(1, k+1):
        selected_nums.append(i)
        find_per(cnt+1)
        selected_nums.pop()


find_per(0)