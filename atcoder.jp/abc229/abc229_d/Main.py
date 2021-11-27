import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import ceil, floor, sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    s = s_input()
    k = i_input()
    
    dot_l = []

    for i in range(len(s)):
        if s[i] == '.':
            dot_l.append(i)

    len_dot = len(dot_l)

    if len_dot <= k:
        print(len(s))
        exit()

    ans_max = 0

    for i in range(len(dot_l)):
        if i != 0:
            before_next = dot_l[i-1]
            before = before_next + 1
        else:
            before = 0
            
        if i + k >= len(dot_l):
            after = len(s) - 1
        else:
            after_next = dot_l[i+k]
            after = after_next - 1

        ans_max = max(ans_max, after - before + 1)

        if i - k < 0:
            before = 0
        else:
            before_next = dot_l[i-k]
            before = before_next + 1

        if i + 1 >= len(dot_l):
            after = len(s) - 1
        else:
            after_next = dot_l[i+1]
            after = after_next - 1

        ans_max = max(ans_max, after - before + 1)

    print(ans_max)

if __name__ == '__main__':
    main()
