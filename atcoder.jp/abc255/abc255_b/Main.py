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
    n, k = i_map()
    a_list = i_list()
    num_list = i_row_list(n)

    a_set = set(a_list)

    min_list = [INF] * n 

    for i in range(n):
        if i + 1 in a_set:
            min_list[i] = 0
            continue
        for light in a_list:
            j = light - 1
            tmp_x = abs(num_list[i][0] - num_list[j][0])
            tmp_y = abs(num_list[i][1] - num_list[j][1])
            tmp_ans = pow(tmp_x, 2) + pow(tmp_y, 2)
            min_list[i] = min(min_list[i], tmp_ans)

    ans_max = max(min_list)
    print(pow(ans_max, 0.5))

if __name__ == '__main__':
    main()
