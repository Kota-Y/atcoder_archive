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
    n, q = i_map()
    
    d = defaultdict(int)
    db = defaultdict(int)

    for i in range(q):
        l = i_list()
        if l[0] == 1:
            x = l[1]
            y = l[2]

            d[x] = y
            db[y] = x
        elif l[0] == 2:
            x = l[1]
            y = l[2]

            d[x] = 0
            db[y] = 0
        elif l[0] == 3:
            x = l[1]

            tmp_l = []
            index = x
            while True:
                if db[index] == 0:
                    break
                index = db[index]

            while True:
                if d[index] == 0:
                    tmp_l.append(index)
                    break
                tmp_l.append(index)
                index = d[index]

            print(len(tmp_l), *tmp_l)
            

if __name__ == '__main__':
    main()
