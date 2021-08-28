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
    n, M, K = i_map()
    num_list = i_list()

    tmp_list = []
    for i in range(1, 60):
        tmp_list.append(pow(2, i))

    monster_list = []
    for i in range(n):
        monster_list.append([num_list[i], i])

    count = 0

    ans_list = []

    for m, index in monster_list:
        m_min = m
        i_count = 0
        for i in range(len(tmp_list)):
            if m_min > (m * tmp_list[i])%K:
                m_min = (m * tmp_list[i])%K
                i_count = i + 1
        ans_list.append([i_count, m_min, index])

    ans_list.sort()

    for i, _, index in ans_list:
        if i == 0:
            continue
        if M >= i:
            for _ in range(i):
                print(index, index)
            M -= i
        else:
            m = num_list[index]
            m_min = m
            i_count = 0
            for j in range(M):
                if m_min > (m * tmp_list[j])%K:
                    m_min = (m * tmp_list[j])%K
                    i_count = j + 1
            for _ in range(i_count):
                print(index, index)
            M -= i_count

if __name__ == '__main__':
    main()
