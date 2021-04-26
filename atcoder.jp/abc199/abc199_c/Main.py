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

def main():
    n = i_input()
    s = s_input()
    q = i_input()

    s = list(s)

    hanten_flag = False
    for _ in range(q):
        t, a, b = i_map()
        if t == 2:
            hanten_flag = not hanten_flag
            continue
        if hanten_flag:
            if a <= n:
                a = a + n
            else:
                a = a - n
            if b <= n:
                b = b + n
            else:
                b = b - n
        s[a-1], s[b-1] = s[b-1], s[a-1]
        
    if hanten_flag:
        s = s[n:] + s[:n]
        print(''.join(s))
    else:
        print(''.join(s))

if __name__ == '__main__':
    main()
