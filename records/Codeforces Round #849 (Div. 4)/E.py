"""
    Name    | Kenny Chen
    Contest | Codeforces Round #849 (Div. 4)
    Problem | Negatives and Positives
    Time    | 02/05/2023, 23:43:07
"""
import sys


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
    array = list(map(int, input().split(" ")))
    negative_count = 0
    even_sum = 0
    min = sys.maxsize
    min_index = 0
    for i in range(length):
        even_sum += abs(array[i])
        if array[i] < 0:
            negative_count += 1

        if abs(array[i]) < min:
            min = abs(array[i])
            min_index = i

    if negative_count % 2 == 0:
        print(even_sum)
    else:
        print(even_sum - min * 2)
