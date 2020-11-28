import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
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
    n, k = i_map()
    s = s_input()

    if n == 1:
        print(s)
        exit()

    S = ''
    if n < 2**min(22, k):
        S = s * ceil(2**min(22, k) / n)
    else:
        S = s

    S = S[:2**min(22, k)]

    s_que = deque(S)

    for _ in range(2**min(22, k)-1):
        left = s_que.popleft()
        right = s_que.popleft()
        if left == 'R':
            if right == 'P':
                s_que.append('P')
            else:
                s_que.append('R')
        elif left == 'S':
            if right == 'R':
                s_que.append('R')
            else:
                s_que.append('S')
        elif left == 'P':
            if right == 'S':
                s_que.append('S')
            else:
                s_que.append('P')

    print(s_que[0])

if __name__ == '__main__':
    main()
