"""
    Name    | Kenny Chen
    Contest | Codeforces Round #849 (Div. 4)
    Problem | Codeforces Checking
    Time    | 02/05/2023, 23:42:56
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
    s = "codeforces"
    test = input()
    print("YNEOS"[test not in s :: 2])
