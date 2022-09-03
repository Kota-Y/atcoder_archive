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
    n, m = i_map()
    num_list = i_list()
    
    ruisekiwa = list(accumulate(num_list))

    ans_max = 0
    for i in range(m):
        ans_max += num_list[i]  * (i+1)

    tmp =  ans_max

    for i in range(n-m):
        tmp -= num_list[i]
        tmp += num_list[i+m] * m
        tmp -= ruisekiwa[i+m-1] - ruisekiwa[i]
        ans_max = max(ans_max, tmp)

    tmp = 0
    for i in range(m):
        tmp += num_list[n-m+i] * (i+1)
    ans_max = max(ans_max, tmp)

    print(ans_max)

if __name__ == '__main__':
    main()
