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
    b_list = i_list()
    
    q = deque()

    a = a_list[0]
    b = b_list[0]

    q.append(a)
    q.append(b)

    for i in range(n-1):
        if len(q) == 0:
            print('No')
            exit()

        a_n = a_list[i+1]
        b_n = b_list[i+1]

        append_set = set()

        while len(q) != 0:
            tmp = q.pop()
            if abs(tmp - a_n) <= k:
                append_set.add(a_n)
            if abs(tmp - b_n) <= k:
                append_set.add(b_n)

        for apppend in append_set:
            q.append(apppend)
            
        if len(q) == 0:
            print('No')
            exit()

    print('Yes')

if __name__ == '__main__':
    main()
