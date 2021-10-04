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
    h, w = i_map()
    num_list = i_row_list(h)

    ans_max = 0

    for bit in product([0,1], repeat=h):
        bit_num = bit.count(1)
        cnt = Counter()
        for i in range(w):
            tmp_set = set()
            for j in range(h):
                if bit[j] == 1:
                    tmp_set.add(num_list[j][i])
            if len(tmp_set) == 1:
                l = list(tmp_set)
                cnt[l[0]] += 1
        
        tmp_max = max(cnt.values()) * bit_num if len(cnt) > 0 else 0
        ans_max = max(ans_max, tmp_max)
 
    print(ans_max)

if __name__ == '__main__':
    main()
