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
    x, y = i_map()
    a_list = i_list()
    b_list = i_list()

    ans = 0

    a_port = True
    cu_time = a_list[0]
    while True:
        if a_port:
            b_time = cu_time + x
            insert_index = bisect_left(b_list, b_time)
            if insert_index >= m:
                break
            cu_time = b_list[insert_index]
            a_port = not a_port
            ans += 1
        else:
            a_time = cu_time + y
            insert_index = bisect_left(a_list, a_time)
            if insert_index >= n:
                break
            cu_time = a_list[insert_index]
            a_port = not a_port

    print(ans)

if __name__ == '__main__':
    main()
