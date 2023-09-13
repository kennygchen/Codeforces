"""
    Name    | Kenny Chen
    Contest | Codeforces Round #849 (Div. 4)
    Problem | Following Directions
    Time    | 02/05/2023, 23:43:00
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
    start = [0, 0]
    goal = [1, 1]
    length = input()
    s = input()
    candy = 0
    for move in s:
        if move == "U":
            start[1] += 1
        elif move == "D":
            start[1] -= 1
        elif move == "L":
            start[0] -= 1
        elif move == "R":
            start[0] += 1

        if start[0] == 1 and start[1] == 1:
            candy = 1
    if candy:
        print("YES")
    else:
        print("NO")
