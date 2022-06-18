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
    h1, h2, h3, w1, w2, w3 = i_map()

    max_num = max(h1, h2, h3, w1, w2, w3)
    
    ans = 0

    for math00 in range(1, max_num-1):
        for math01 in range(1, max_num-1):
            math02 = h1 - math00 - math01
            if math02 < 1:
                continue
            for math10 in range(1, max_num-1):
                math20 = w1 - math00 - math10
                if math20 < 1:
                    continue
                for math11 in range(1, max_num-1):
                    math21 = w2 - math01 - math11
                    if math21 < 1:
                        continue  
                    math12 = h2 - math10 - math11
                    if math12 < 1:
                        continue  
                    tmp_h = h3 - math20 - math21
                    tmp_w = w3 - math02 - math12
                    if tmp_h < 1 or tmp_w < 1:
                        continue
                    if tmp_h == tmp_w:
                        ans += 1
                                  
    print(ans)

if __name__ == '__main__':
    main()
