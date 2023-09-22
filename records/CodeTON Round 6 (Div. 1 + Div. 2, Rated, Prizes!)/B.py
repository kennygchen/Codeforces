"""
    Name    | Kenny Chen
    Contest | CodeTON Round 6 (Div. 1 + Div. 2, Rated, Prizes!)
    Problem | Friendly Arrays
    Time    | 09/18/2023, 07:35:35
"""
import sys

input = sys.stdin.readline

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
    n, m = intList()
    a = intList()
    b = intList()

    min_res, max_res = 999999, -999999
    ans = a[0]
    for i in range(1, len(a)):
        ans = ans ^ a[i]
    print(ans)

    for j in range(len(b)):
        a1 = a.copy()
        min_res, max_res = 999999, -999999
        for i in range(len(a)):
            a1[i] = a1[i] | b[j]
        ans = a1[0]
        for i in range(1, len(a)):
            ans = ans ^ a1[i]
        if ans < min_res:
            min_res = ans
        if ans > max_res:
            max_res = ans

    print(str(min_res) + " " + str(max_res))
