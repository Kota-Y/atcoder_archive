import sys, re
from math import ceil, floor, sqrt, pi, factorial#, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_list(N): return [s_list() for _ in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n, a, b, c = i_map()
    num_list = i_row(n)

    min_mp = INF
    for bin in list(product([0, 1, 2, 3], repeat=n)):
        ac = bin.count(1)
        bc = bin.count(2)
        cc = bin.count(3)
        if ac < 1 or bc < 1 or cc < 1:
            continue
        mp = 0
        if ac >= 2:
            mp += 10 * (ac-1)
        if bc >= 2:
            mp += 10 * (bc-1)
        if cc >= 2:
            mp += 10 * (cc-1)
        sum_a, sum_b, sum_c = 0, 0, 0
        for i in range(n):
            if bin[i] == 1:
                sum_a += num_list[i]
            elif bin[i] == 2:
                sum_b += num_list[i]
            elif bin[i] == 3:
                sum_c += num_list[i]
        mp += abs(a-sum_a)
        mp += abs(b-sum_b)
        mp += abs(c-sum_c)
        min_mp = min(min_mp, mp)
            
    print(min_mp)

if __name__ == '__main__':
    main()
