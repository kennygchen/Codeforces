"""
    Name    | Kenny Chen
    Contest | Codeforces Beta Round 4 (Div. 2 Only)
    Problem | Watermelon
    Time    | 09/13/2023, 15:44:45
"""
import sys

input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():  # For taking integer inputs
    return int(input())


def inlt():  # For taking integer inputs
    return list(map(int, input().split()))


def insr():  # For taking string inputs
    s = input()
    return list(s[: len(s) - 1])


def invr():  # For taking space seperated integer variable inputs
    return map(int, input().split())


def __main__():
    input = inp()
    if input == 2:
        print("NO")
    else:
        print("YES" if input % 2 == 0 else "NO")


if __name__ == "__main__":
    __main__()
