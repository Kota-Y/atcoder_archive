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

def rotate(l: list) -> list:
    return list(zip(*l[::-1]))

def find_left_top(l, n):
    for i in range(n):
        for j in range(n):
            if l[i][j]=='#':
                return i, j

def is_same(s_list, t_list, n):
    si,sj = find_left_top(s_list, n)
    ti,tj = find_left_top(t_list, n)
    offset_i = ti-si
    offset_j = tj-sj
    for i in range(n):
        for j in range(n):
            ii = i+offset_i
            jj = j+offset_j
            if 0 <= ii < n and 0 <= jj < n:
                if s_list[i][j] != t_list[ii][jj]:
                    return False
            else:
                if s_list[i][j]=='#':
                    return False
    return True    

def main():
    n = i_input()
    s_list = s_row_list(n)
    t_list = s_row_list(n)
    
    count_s = 0
    count_t = 0
    for i in range(n):
        for j in range(n):
            if s_list[i][j] == '#':
                count_s += 1
            if t_list[i][j] == '#':
                count_t += 1           

    if count_s != count_t:
        print('No')
        exit()

    for _ in range(4):
        if is_same(s_list, t_list, n):
            print('Yes')
            exit()
        s_list = rotate(s_list)

    print('No')

if __name__ == '__main__':
    main()
