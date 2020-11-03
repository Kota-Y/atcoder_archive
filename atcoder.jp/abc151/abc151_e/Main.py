import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def nCr(n: int, r: int, factorial: list, inverse: list) -> int:
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD

def main():
    n, k = i_map()
    num_list = i_list()

    num_list.sort()

    factorial = [1]
    inverse = [1]
    for i in range(1, n+2):
        factorial.append(factorial[-1] * i % MOD)
        inverse.append(pow(factorial[-1], MOD - 2, MOD))

    ans = 0
    for i in range(n - k + 1):
        ans -= num_list[i] * nCr(n - i - 1, k - 1, factorial, inverse) % MOD
        ans %= MOD

    num_list.sort(reverse=True)
    for i in range(n - k + 1):
        ans += num_list[i] * nCr(n - i - 1, k - 1, factorial, inverse) % MOD
        ans %= MOD
            
    print(ans % MOD)
    
if __name__ == '__main__':
    main()
