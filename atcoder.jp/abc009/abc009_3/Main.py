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
    n, k = i_map()
    s = s_input()
    
    ans = list(s)

    for i in range(n):
        l = i
        for j in range(i+1, n):
            # 現在の i 番目の文字より小さい文字があるか探す
            if ans[l] > ans[j]:
                # あった
                ss = ans.copy()
                ss[i], ss[j] = ss[j], ss[i]
                # ss と比較したとき、違う数
                diff = 0
                for t in range(n):
                    if ss[t] != s[t]:
                        diff += 1
                if diff <= k:
                    l = j
        ans[i], ans[l] = ans[l], ans[i]

    print("".join(ans))

if __name__ == '__main__':
    main()
