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
num_list = []
str_list = []

def main():
    n, m = i_map()
    for i in range(m):
        p, y = i_map()
        num_list.append([p, y, i])

    sorted_data = sorted(num_list, key=lambda x: x[1])
    sorted_data = sorted(sorted_data, key=lambda x: x[0])

    ans_list = []
    count_index = 0
    for num in sorted_data:
        if count_index != num[0]:
            count_index = num[0]
            count_num = 1
        else:
            count_num += 1
        ans_num = str(num[0]).zfill(6) + str(count_num).zfill(6)
        ans_list.append([num[2], ans_num])

    ans_list.sort()

    for ans in ans_list:
        print(ans[1])
 
if __name__ == '__main__':
    main()
