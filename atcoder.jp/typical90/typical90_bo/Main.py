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

def Base_n_to_10(value, base):
    return int(str(value), base)

def Base_10_to_n(value, base):
    nine_number = ""
    while value > 0:
        nine_number += str(value % base)
        value //= base
    return int(nine_number[::-1])

def main():
    n8, k = i_map()

    if n8 == 0:
        print(0)
        exit()

    for _ in range(k):
        n9 = int(Base_10_to_n(int(Base_n_to_10(n8, 8)), 9))
        tmp_9 = ''
        for i in range(len(str(n9))):
            if str(n9)[i] == '8':
                tmp_9 += '5'
            else:
                tmp_9 += str(n9)[i]
        n8 = int(tmp_9)

    print(n8)

if __name__ == '__main__':
    main()
