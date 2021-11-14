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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def f(a, b, c, d):
    return abs(a-c) + abs(b-d)

def main():
    num_list = i_row_list(1000)
    
    distance_list = []
    for i, (a, b, c, d) in enumerate(num_list):
        distance_list.append((f(a, b, c, d), i))

    zero = []
    one = []
    two = []
    three = []
    for i, (a, b, _, _) in enumerate(num_list):
        if a >= 400 and b >= 400:
            zero.append((distance_list[i][0], i))
        elif a < 400 and b >= 400:
            one.append((distance_list[i][0], i))
        elif a < 400 and b < 400:
            two.append((distance_list[i][0], i))
        elif a >= 400 and b < 400:
            three.append((distance_list[i][0], i))

    zero.sort()
    one.sort()
    two.sort()
    three.sort()

    zero_sum_top50 = 0
    one_sum_top50 = 0
    two_sum_top50 = 0
    three_sum_top50 = 0

    if len(zero) >= 50:
        for distance, _ in zero:
            zero_sum_top50 += distance
    if len(one) >= 50:
        for distance, _ in one:
            one_sum_top50 += distance
    if len(two) >= 50:   
        for distance, _ in two:
            two_sum_top50 += distance
    if len(three) >= 50:
        for distance, _ in three:
            three_sum_top50 += distance

    if zero_sum_top50 <= one_sum_top50 and zero_sum_top50 <= two_sum_top50 and zero_sum_top50 <= three_sum_top50:
        delivery_list = deepcopy(zero[:50])
    if one_sum_top50 <= zero_sum_top50 and one_sum_top50 <= two_sum_top50 and one_sum_top50 <= three_sum_top50:
        delivery_list = deepcopy(one[:50])
    if two_sum_top50 <= zero_sum_top50 and two_sum_top50 <= one_sum_top50 and two_sum_top50 <= three_sum_top50:
        delivery_list = deepcopy(two[:50])
    if three_sum_top50 <= zero_sum_top50 and three_sum_top50 <= one_sum_top50 and three_sum_top50 <= two_sum_top50:
        delivery_list = deepcopy(three[:50])

    output1_list = [50]
    tmp_list = []
    for _, delivery in delivery_list:
        tmp_list.append(delivery+1)
    tmp_list.sort()

    for tmp in tmp_list:
        output1_list.append(tmp)
    print(*output1_list)

    output2_list = [102, 400, 400]

    visit_list = []
    for _, delivery in delivery_list:
        a, b = num_list[delivery][0], num_list[delivery][1]
        visit_list.append([a, b, delivery])

    cur = [400, 400]
    tmp_list = []
    while len(tmp_list) != 200:
        tmp_min = INF
        tmp_xy = []
        tmp_index = -1
        tmp_i = -1
        for i, (a, b, delivery_i) in enumerate(visit_list):
            if delivery_i == -11:
                continue
            if tmp_min > f(cur[0], cur[1], a, b):
                tmp_min = f(cur[0], cur[1], a, b)
                tmp_xy = [a, b]
                tmp_index = delivery_i
                tmp_i = i
        tmp_list.append(tmp_xy[0])
        tmp_list.append(tmp_xy[1])
        if tmp_index != -1:
            visit_list.append([num_list[tmp_index][2], num_list[tmp_index][3], -1])
        visit_list[tmp_i][2] = -11

    for tmp in tmp_list:
        output2_list.append(tmp)

    output2_list.append(400)
    output2_list.append(400)
    print(*output2_list)

if __name__ == '__main__':
    main()
