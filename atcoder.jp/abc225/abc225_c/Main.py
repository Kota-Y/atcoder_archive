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
    n, m = i_map()
    num_list = i_row_list(n)

    for i in range(n-1):
        for j in range(m):
            if num_list[i][j] + 7 != num_list[i+1][j]:
                print('No')
                exit()

    for i in range(m-1):
        for j in range(n):
            if num_list[j][i] + 1 != num_list[j][i+1]:
                print('No')
                exit()

    for i in range(7):
        tmp = (num_list[0][0]-i) / 7
        if tmp.is_integer():
            ans = i

    if ans == 0 and m != 1: 
        print('No')
        exit()

    if ans + m > 8:
        print('No')
        exit()

    print('Yes')

if __name__ == '__main__':
    main()
