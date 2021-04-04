import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, atan2, sin, cos
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
    n = i_input()
    x0, y0 = i_map()
    x, y = i_map()
    
    center_x = (x + x0) / 2
    center_y = (y + y0) / 2
    r = pow(pow(x-x0, 2) + pow(y-y0, 2), 0.5) / 2

    # 中心から(x1,y1)への角度
    angle_0 = atan2(y0 - center_y, x0 - center_x)
    angle_tmp = 2 * pi / n
    angle_target = angle_0 + angle_tmp

    # x1,y1の座標を求める
    x1 = center_x + r * cos(angle_target)
    y1 = center_y + r * sin(angle_target)

    print(x1,y1)

if __name__ == '__main__':
    main()
