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
    s = s_input()
    t = i_input()

    up = 0
    down = 0
    left = 0
    right = 0
    hatena = 0

    for muki in s:
        if muki == 'U':
            up += 1
        elif muki == 'D':
            down += 1
        elif muki == 'L':
            left += 1  
        elif muki == 'R':
            right += 1
        else:
            hatena += 1
 
    if t == 1:
        ans = max(up-down, down-up)+max(left-right, right-left) + hatena
        print(ans)
    else:
        ans = max(up-down, down-up)+max(left-right, right-left) - hatena
        if ans >= 0:
            print(ans)
        else:
            print(0 if ans % 2 == 0 else 1)

if __name__ == '__main__':
    main()
