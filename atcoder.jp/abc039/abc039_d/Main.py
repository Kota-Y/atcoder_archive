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
    h, w = i_map()
    s_list = s_row_list(h)

    before_list = [['#'] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s_list[i][j] == '#':
                continue
            before_list[i][j] = '.'
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]):
                ni = i + dx
                nj = j + dy
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                before_list[ni][nj] = '.'

    after_list = [['.'] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if before_list[i][j] == '.':
                continue
            after_list[i][j] = '#'
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]):
                ni = i + dx
                nj = j + dy
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                after_list[ni][nj] = '#' 

    for i in range(h):
        for j in range(w):
            if s_list[i][j] != after_list[i][j]:
                print('impossible')
                exit()

    print('possible')
    for i in range(h):
        for j in range(w):
            print(before_list[i][j], end='')
        print()

if __name__ == '__main__':
    main()
