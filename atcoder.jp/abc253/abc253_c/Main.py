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
    q = i_input()

    max_q = []
    min_q = []

    heapify(max_q)
    heapify(min_q)
    d = defaultdict(int)

    for _ in range(q):
        input_l = i_list()
        if input_l[0] == 1:
            x = input_l[1]
            if d[x] == 0:
                heappush(max_q, -x)
                heappush(min_q, x)
            d[x] += 1
        elif input_l[0] == 2:
            x, c = input_l[1], input_l[2]
            tmp_x_co = d[x]
            d[x] -= min(c, tmp_x_co)
        elif input_l[0] == 3:
            max_num = -1
            while max_num == -1:
                max_num = heappop(max_q) * -1
                if d[max_num] == 0:
                    max_num = -1

            min_num = -1
            while min_num == -1:
                min_num = heappop(min_q)
                if d[min_num] == 0:
                    min_num = -1

            print(max_num - min_num)

            heappush(max_q, -max_num)
            heappush(min_q, min_num)

if __name__ == '__main__':
    main()
