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
def s_row(N): return [s_input for _ in range(N)]
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
    num_list = i_list()

    money = 1000
    stock = 0
    buy_flag = True
    sale_flag = False

    for day in range(n):
        today_info = num_list[day]
        if buy_flag:
            buy_flag = False
            for feature in range(day+1,n):
                feature_info = num_list[feature]
                if today_info < feature_info:
                    for min_day in range(day+1, feature):
                        if today_info > num_list[min_day]:
                            break
                    else:
                        buy_flag = True
                    break
            if buy_flag:
                buy_num = money // today_info
                money -= buy_num * today_info
                stock += buy_num
                buy_flag = False
                sale_flag = True
            else:
                buy_flag = True
        elif sale_flag:
            for feature in range(day+1,n):
                feature_info = num_list[feature]
                if feature_info > today_info:
                    for min_day in range(day+1, feature):
                        if today_info > num_list[min_day]:
                            break
                    else:
                        sale_flag = False
                    break
            if sale_flag:
                money += today_info * stock
                stock = 0
                buy_flag = True
                sale_flag = False
            else:
                sale_flag = True

        # print(day+1, money, stock)

    print(money)

if __name__ == '__main__':
    main()
