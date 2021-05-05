import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
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
    n = i_input()
    a_list = i_row_list(n)
    m = i_input()
    x_list = []
    for _ in range(m):
        x, y = i_map()
        x_list.append(str(x-1)+str(y-1))
        x_list.append(str(y-1)+str(x-1))

    l = [i for i in range(n)]
    
    min_ans = INF
    for v in permutations(l):
        tmp = 0
        s = ''
        for tmp_v in v:
            s += str(tmp_v)
        for x in x_list:
            if x in s:
                break
        else:              
            for i in range(n):
                tmp += a_list[v[i]][i]
            min_ans = min(min_ans, tmp)

    print(min_ans if min_ans != INF else -1)

if __name__ == '__main__':
    main()
