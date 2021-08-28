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
    num_list = i_row_list(n)
    
    ans_a = 0
    flag = True
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                ans_a += num_list[i][j]
            elif i % 2 != 0 and j % 2 != 0:
                ans_a += num_list[i][j]

    ans_b = 0
    flag = False
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 != 0:
                ans_b += num_list[i][j]
            elif i % 2 != 0 and j % 2 == 0:
                ans_b += num_list[i][j]

    if ans_a >= ans_b:
        for i in range(n):
            for j in range(n):
                if i % 2 == 0 and j % 2 == 0:
                    print(1, end=' ')
                elif i % 2 != 0 and j % 2 != 0:
                    print(1, end=' ')
                else:
                    print(0, end=' ')
            print()
    else:
        for i in range(n):
            for j in range(n):
                if i % 2 == 0 and j % 2 != 0:
                    print(1, end=' ')
                elif i % 2 != 0 and j % 2 == 0:
                    print(1, end=' ')
                else:
                    print(0, end=' ')
            print()
                
if __name__ == '__main__':
    main()
