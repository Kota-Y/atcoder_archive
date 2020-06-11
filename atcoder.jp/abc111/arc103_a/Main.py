import sys, re
from math import ceil, floor, sqrt, pi, factorial#, gcd
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
    n = i_input()
    num_list = i_list()

    zero_list = []
    one_list = []
    for i in range(n):
        if i % 2 == 0:
            zero_list.append(num_list[i])
        else:
            one_list.append(num_list[i])

    zero_c = Counter(zero_list)
    one_c = Counter(one_list)

    zero_saihin_key = zero_c.most_common()[0][0]
    zero_saihin_val = zero_c.most_common()[0][1]
    one_saihin_key = one_c.most_common()[0][0]
    one_saihin_val = one_c.most_common()[0][1]

    if zero_saihin_key != one_saihin_key:
        print(n - zero_saihin_val - one_saihin_val)
        exit()

    if num_list.count(zero_saihin_key) == n:
        print(n//2)
        exit()

    if len(zero_c) == 1:
        zero_saihin_val2 = zero_saihin_val
    else:
        zero_saihin_val2 = zero_c.most_common()[1][1]

    if len(one_c) == 1:
        one_saihin_val2 = one_saihin_val
    else:
        one_saihin_val2 = one_c.most_common()[1][1]

    count1 = n - zero_saihin_val - one_saihin_val2
    count2 = n - zero_saihin_val2 - one_saihin_val

    print(min(count1, count2))

if __name__ == '__main__':
    main()
