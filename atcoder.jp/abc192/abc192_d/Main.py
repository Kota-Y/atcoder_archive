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

def get_n(n, base_x):
    s_n = str(n)
    len_n = len(s_n)
    ans = 0
    for i in range(len_n):
        ans += pow(base_x, len_n-i-1) * int(s_n[i])
    return ans

def main():
    x = i_input()
    m = i_input()
    
    if len(str(x)) == 1:
        print(1 if x <= m else 0)
        exit()

    s_x = str(x)
    max_d = 0
    for s in s_x:
        max_d = max(max_d, int(s))

    left = max_d
    right = m+1
    while left + 1 < right:
        middle = (left+right) // 2
        b = get_n(x, middle)
        if b <= m:
            left = middle
        elif b > m:
            right = middle

    print(left-max_d)

if __name__ == '__main__':
    main()
