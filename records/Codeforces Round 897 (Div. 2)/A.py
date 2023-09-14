"""
    Name    | Kenny Chen
    Contest | Codeforces Round 897 (Div. 2)
    Problem | green_gold_dog, array and permutation
    Time    | 09/13/2023, 16:16:16
"""
############ ---- Input Functions ---- ############
def intList():  # For taking List inputs
    return list(map(int, input().split()))


def testCases(num=False):
    i = input().split()
    if num:
        return int(i[0])
    try:
        return list(map(int, i))
    except Exception:
        return i


for tc in range(testCases(1)):
    n = int(input())
    array = intList()
    arr = [None] * n
    for i, num in enumerate(array):
        arr[i] = (num, i)

    arr = sorted(arr, reverse=True)
    ans = [None] * n
    for i in range(n):
        ans[arr[i][1]] = i + 1
    for a in ans:
        print(str(a), end=" ")
    print()
