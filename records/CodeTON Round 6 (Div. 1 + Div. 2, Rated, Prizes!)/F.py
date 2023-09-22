"""
    Name    | Kenny Chen
    Contest | CodeTON Round 6 (Div. 1 + Div. 2, Rated, Prizes!)
    Problem | Lazy Numbers
    Time    | 09/18/2023, 07:36:16
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
    # Write your code here
    pass
