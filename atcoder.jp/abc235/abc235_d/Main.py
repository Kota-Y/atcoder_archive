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

a, n = i_map()

ans_list = [-1] * 100000000

ans_list[1] = 0

def f(num, count):
    count += 1

    if num >= 10 and num % 10 != 0:
        tmp_s = str(num)
        swap_num = int(tmp_s[-1] + tmp_s[:len(tmp_s)-1])

        if swap_num < 1000000:
            if ans_list[swap_num] == -1 or ans_list[swap_num] > count:
                ans_list[swap_num] = count
                f(swap_num, count)
    
    index_num = num * a

    if 1000000 < index_num:
        return 0

    if index_num < 100000000:
        ans_list[index_num] = count

    f(index_num, count)

f(1, 0)
    
print(ans_list[n])
