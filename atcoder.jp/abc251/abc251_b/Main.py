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
    n, w = i_map()
    num_list = i_list()
    
    if n == 1:
        if num_list[0] <= w:
            print(1)
        else:
            print(0)
        exit()

    ans_set = set()

    if n == 2:
        for bit in product([0,1], repeat=2):
            tmp = 0
            for i in range(2):
                if bit[i] == 1:
                    tmp += num_list[i]
            if tmp <= w:
                if tmp == 0:
                    continue
                ans_set.add(tmp)
        print(len(ans_set))
        exit()

    for i in range(n-2):
        a = num_list[i]
        if a <= w:
            ans_set.add(a)
        for j in range(i+1, n-1):
            b = num_list[j]
            if b <= w:
                ans_set.add(b)
            tmp_ab = a + b
            if tmp_ab <= w:
                ans_set.add(tmp_ab)
            for k in range(j+1, n):
                c = num_list[k]
                tmp_ac = a + c
                tmp_bc = b + c
                tmp_abc = a + b + c
                if c <= w:
                    ans_set.add(c)
                if tmp_ac <= w:
                    ans_set.add(tmp_ac)
                if tmp_bc <= w:
                    ans_set.add(tmp_bc)
                if tmp_abc <= w:
                    ans_set.add(tmp_abc)                  

    print(len(ans_set))

if __name__ == '__main__':
    main()
