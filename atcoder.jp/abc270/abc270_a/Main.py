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
    a, b = i_map()
    
    sa = '000'
    if a == 1:
        sa = '100'
    elif a == 2:
        sa = '010'
    elif a == 3:
        sa = '110'
    elif a == 4:
        sa = '001'
    elif a == 5:
        sa = '101'
    elif a == 6:
        sa = '011'
    elif a == 7:
        sa = '111'

    sb = '000'
    if b == 1:
        sb = '100'
    elif b == 2:
        sb = '010'
    elif b == 3:
        sb = '110'
    elif b == 4:
        sb = '001'
    elif b == 5:
        sb = '101'
    elif b == 6:
        sb = '011'
    elif b == 7:
        sb = '111'

    ans = int(sa) | int(sb)

    if ans == 0:
        print(0)
    elif ans == 1:
        print(4)
    elif ans == 11:
        print(6)
    elif ans == 111:
        print(7)
    elif ans == 10:
        print(2)
    elif ans == 100:
        print(1)
    elif ans == 101:
        print(5)
    elif ans == 110:
        print(3)    

if __name__ == '__main__':
    main()
