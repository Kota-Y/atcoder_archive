import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, cos, radians
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
input = sys.stdin.readline 
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
    a, b, h, m = i_map()

    minitus = 6 * m
    hours = 30 * h + 0.5 * m

    if abs(hours-minitus) > 180:
        theta = 360 - abs(hours-minitus)
    else:
        theta = abs(hours-minitus)

    ans2 = pow(a,2) + pow(b,2) - 2 * a * b * cos(radians(theta))

    print(pow(ans2,0.5))

if __name__ == '__main__':
    main()
