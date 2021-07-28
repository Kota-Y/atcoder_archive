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
    h, w = i_map()
    a_list = i_row_list(h)
    b_list = i_row_list(h)

    ans = 0

    for i in range(h-1):
        for j in range(w-1):
            if a_list[i][j] == b_list[i][j]:
                continue
            tmp = b_list[i][j] - a_list[i][j]
            a_list[i][j] += tmp
            a_list[i+1][j] += tmp
            a_list[i][j+1] += tmp
            a_list[i+1][j+1] += tmp
            ans += abs(tmp)

    for i in range(h):
        for j in range(w):
            if a_list[i][j] != b_list[i][j]:
                print('No')
                exit()

    print('Yes')
    print(ans)

if __name__ == '__main__':
    main()
