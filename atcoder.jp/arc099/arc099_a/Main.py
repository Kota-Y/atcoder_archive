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
    n, k = i_map()
    num_list = i_list()

    if n == k:
        print(1)
        exit()

    one_index = 0

    for i in range(n):
        if num_list[i] == 1:
            one_index = i
            break

    left_num = one_index
    right_num = n - one_index - 1

    count = 0

    left = left_num // (k-1)
    right = right_num // (k-1)

    count += left + right

    amari = n - 1 - (k-1) * (left+right)

    if amari > k - 1:
        count += 2
    elif amari == 0:
        pass
    else:
        count += 1
        
    print(count)

if __name__ == '__main__':
    main()
