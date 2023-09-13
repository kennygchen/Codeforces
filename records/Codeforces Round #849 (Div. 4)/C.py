"""
    Name    | Kenny Chen
    Contest | Codeforces Round #849 (Div. 4)
    Problem | Prepend and Append
    Time    | 02/05/2023, 23:43:01
"""


def ii(num=False):
    i = input().split()
    if num:
        return int(i[0])
    try:
        return list(map(int, i))
    except Exception:
        return i


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


for _ in range(ii(1)):
    length = ii(1)
    s = input()
    answer = length
    left = 0
    right = length - 1

    while s[left] != s[right] and answer > 0:
        left += 1
        right -= 1
        answer -= 2
    print(answer)
