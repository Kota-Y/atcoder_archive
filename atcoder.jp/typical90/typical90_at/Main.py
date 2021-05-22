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
    n = i_input()
    num_list = i_row_list(3)

    a_list = []
    b_list = []
    c_list = []
    for i in range(n):
        a_list.append(num_list[0][i]%46)
        b_list.append(num_list[1][i]%46)
        c_list.append(num_list[2][i]%46)

    a_co = Counter(a_list)
    b_co = Counter(b_list)
    c_co = Counter(c_list)

    ans = 0

    for i in range(46):
        for j in range(46):
            for k in range(46):
                a_num = a_co[i]
                b_num = b_co[j]
                c_num = c_co[k]
                if (i + j + k) % 46 != 0:
                    continue
                ans += a_num * b_num * c_num
    
    print(ans)

if __name__ == '__main__':
    main()
