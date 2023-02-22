"""
    Name    | Kenny Chen
    Contest | Codeforces Round #849 (Div. 4)
    Problem | Distinct Split
    Time    | 02/05/2023, 23:43:06
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
    n = ii(1)
    s = input()
    ans = 0
    sa = set()
    sb = set()
    pre1 = []
    pre2 = []

    for i in range(n):
        sa.add(s[i])
        sb.add(s[n - i - 1])
        pre1.append(len(sa))
        pre2.append(len(sb))
    pre2.reverse()

    for i in range(n - 1):
        ans = max(ans, pre1[i] + pre2[i + 1])
    print(ans)
