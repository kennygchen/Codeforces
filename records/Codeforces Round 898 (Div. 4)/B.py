"""
    Name    | Kenny Chen
    Contest | Codeforces Round 898 (Div. 4)
    Problem | Good Kid
    Time    | 09/22/2023, 11:05:22
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
    n = input()
    a = intList()
    index = a.index(min(a))
    ans = 1
    for i, d in enumerate(a):
        if i == index:
            d += 1
        ans *= d

    print(ans)
