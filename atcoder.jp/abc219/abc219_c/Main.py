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

def swap_str(s_org, s1, s2, temp='*q@w-e~r^'):
    return s_org.replace(s1, temp).replace(s2, s1).replace(temp, s2)

def main():
    x = s_input()
    n = i_input()
    str_list = s_row(n)

    al = ascii_lowercase

    ans_list = []

    d = dict()
    for i in range(len(x)):
        d[x[i]] = al[i]

    for s in str_list:
        ans_list.append(s.translate(str.maketrans(d)))

    ans_list.sort()

    d = dict()
    for i in range(len(x)):
        d[al[i]] = x[i]
    for s in ans_list:
        print(s.translate(str.maketrans(d)))

if __name__ == '__main__':
    main()
