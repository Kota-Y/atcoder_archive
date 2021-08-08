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
    h, w, n = i_map()

    num_list = []
    for i in range(n):
        a, b = i_map()
        num_list.append([a, b, i])

    num_list.sort()

    ruiseki = [num_list[0][0]-1]
    for i in range(1, n):
        if num_list[i][0] != num_list[i-1][0]:
            tmp = num_list[i][0] - num_list[i-1][0] - 1
        else:
            tmp = 0
        ruiseki.append(ruiseki[i-1]+tmp) 
    for i in range(n):
        num_list[i][0] -= ruiseki[i]

    num_list = sorted(num_list, key=lambda x: x[1])
    
    ruiseki = [num_list[0][1]-1]
    for i in range(1, n):
        if num_list[i][1] != num_list[i-1][1]:
            tmp = num_list[i][1] - num_list[i-1][1] - 1
        else:
            tmp = 0
        ruiseki.append(ruiseki[i-1]+tmp) 
    for i in range(n):
        num_list[i][1] -= ruiseki[i]

    num_list = sorted(num_list, key=lambda x: x[2])
    for a, b, _ in num_list:
        print(a, b)

if __name__ == '__main__':
    main()
