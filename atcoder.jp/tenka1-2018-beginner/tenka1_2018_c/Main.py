import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from array import array
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
def ceil(a, b): return (a + b - 1) // b
def floor(a, b): return a // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n = i_input()
    num_list = i_row(n)

    num_list.sort()

    if n % 2 == 0:
        plus = num_list[n//2:]
        minus = num_list[:n//2]

        result = 2 * sum(plus) - 2 * sum(minus)

        # 足す数は一番小さいものを、
        # 引く数は一番大きいものを端に持っていく
        result = result - plus[0] + minus[-1]
    else:
        plus = num_list[n//2+1:]
        minus = num_list[:n//2]
        mid = num_list[n//2]

        tmp_r = 2 * sum(plus) - 2 * sum(minus)

        # 中央の数を足す方にする場合（大小大小～の並びになる）
        # 両端が足す数になる。足す数のうち小さいものから順に 2個
        # 端に移動するが、そのうち1つは中央の数
        res1 = (tmp_r + mid * 2) - mid - plus[0]

        # 中央の数を引く方にする場合（小大小大～の並びになる）
        # 両端が引く数に（以下略
        res2 = (tmp_r - mid * 2) + mid + minus[-1]

        # 比べて大きい方を取る
        result = max(res1, res2)

    print(result)

if __name__ == '__main__':
    main()
