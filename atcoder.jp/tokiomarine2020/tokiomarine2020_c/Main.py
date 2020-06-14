import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
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
    n, k = i_map()
    num_list = i_list()

    for _ in range(k):
        if num_list.count(n) == n:
            break
        tmp_list = [0] * (n+1)
        for j in range(n):
            l = max(0, j - num_list[j])
            r = min(j + num_list[j]+ 1, n)
            tmp_list[l] += 1
            tmp_list[r] -= 1
        for j in range(n):
            tmp_list[j+1] += tmp_list[j]
        num_list = deepcopy(tmp_list)
        
    print(*num_list[:n])

if __name__ == '__main__':
    main()
