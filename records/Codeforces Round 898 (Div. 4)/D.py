"""
    Name    | Kenny Chen
    Contest | Codeforces Round 898 (Div. 4)
    Problem | 1D Eraser
    Time    | 09/22/2023, 11:05:23
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
    n, k = intList()
    s = input()
    ans = 0
    i = 0
    while i < n:
        if s[i] == "B":
            i = i + k - 1
            ans += 1
        i += 1

    print(ans)