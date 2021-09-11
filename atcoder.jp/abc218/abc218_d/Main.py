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
    n = i_input()
    num_list = i_row_list(n)
    
    l = []

    num_list.sort()

    tmp = num_list[0][0]
    se = {num_list[0][1]}

    for i in range(1, n):
        if tmp == num_list[i][0]:
            se.add(num_list[i][1])
        else:
            if len(se) >= 2:
                l.append(se)
            tmp = num_list[i][0]
            se = {num_list[i][1]}

    if len(se) >= 2:
        l.append(se)

    # print(l)

    ans = 0

    for i in range(len(l)-1):
        tmp_l = list(l[i])
        for k in range(len(l[i])-1):
            tmp1 = tmp_l[k]
            for h in range(k+1, len(l[i])):
                tmp2 = tmp_l[h]
                for j in range(i+1, len(l)):
                    if tmp1 in l[j] and tmp2 in l[j]:
                        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
