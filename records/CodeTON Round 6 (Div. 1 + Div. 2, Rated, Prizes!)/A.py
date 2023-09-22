"""
    Name    | Kenny Chen
    Contest | CodeTON Round 6 (Div. 1 + Div. 2, Rated, Prizes!)
    Problem | MEXanized Array
    Time    | 09/18/2023, 07:35:30
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
    n, k, x = intList()
    if k - x > 1 or n < k:
        print(-1)
        continue
    sum = 0
    count = 0
    for i in range(k):
        sum += i
        count += 1

    while count < n:
        if k < x:
            sum += x
        else:
            sum += k - 1
        count += 1

    print(sum)
