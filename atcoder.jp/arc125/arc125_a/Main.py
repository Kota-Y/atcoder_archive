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
    n, m = i_map()
    S = i_list()
    T = i_list()
    
    S_set = set(S)
    T_set = set(T)
    if S_set & T_set == set() or len(S_set) < len(T_set):
        print(-1)
        exit()
    
    first_digit = S[0]
    right_cnt = 0
    for i in range(n):
        if S[i] != first_digit:
            right_cnt = i
            break
    left_cnt = 0
    for i in range(n - 1, -1, -1):
        if S[i] != first_digit:
            left_cnt = n - i
            break
    second_cnt = min(left_cnt, right_cnt)
    
    ans = 0
    prev = -1
    for i in range(m):
        if prev == -1:
            if T[i] == first_digit:
                ans += 1
            else:
                ans += second_cnt + 1
                prev = T[i]
        else:
            if T[i] == prev:
                ans += 1
            else:
                ans += 2
                prev = T[i]
    print(ans)

if __name__ == '__main__':
    main()
