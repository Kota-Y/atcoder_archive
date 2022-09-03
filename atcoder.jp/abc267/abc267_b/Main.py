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
    s = s_input()

    if s[0] == '1':
        print('No')
        exit()

    l = [1] * 7

    if s[6] == '0':
        l[0] = 0

    if s[3] == '0':
        l[1] = 0

    if s[7] == '0' and s[1] == '0':
        l[2] = 0

    if s[4] == '0' and s[0] == '0':
        l[3] = 0

    if s[8] == '0' and s[2] == '0':
        l[4] = 0

    if s[5] == '0':
        l[5] = 0

    if s[9] == '0':
        l[6] = 0

    before_flag = False
    middle_flag = False
    for i in range(7):
        if before_flag:
            if l[i] == 0:
                middle_flag = True
                before_flag = False
                continue
            else:
                continue

        if middle_flag:
            if l[i] == 1:
                print('Yes')
                exit()
            else:
                continue

        if l[i] == 1:
            before_flag = True
            continue

    print('No')

if __name__ == '__main__':
    main()
