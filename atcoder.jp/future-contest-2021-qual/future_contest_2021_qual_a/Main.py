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
    for i in range(100):
        x, y = i_map()
        tmp = [x, y , i]
        num_list.append(tmp)

    ans = ''

    num_list.sort()

    grid_list = []
    stack_list = []

    for num in num_list:
        x, y = num[0], num[1]
        if x % 2 == 0:
            if len(stack_list) == 0:
                grid_list.append(num)
            else:
                for stack_num in reversed(stack_list):
                    grid_list.append(stack_num)
                stack_list = []
                grid_list.append(num)
        else:
            stack_list.append(num)

    if len(stack_list) != 0:
        for stack_num in reversed(stack_list):
            grid_list.append(stack_num)



    yamafuda =[]
    haichi_list = []

    cx, cy = 0, 0
    for x, y, no in grid_list:
        if x >= 15:
            tmp = [x, y, no]
            haichi_list.append(tmp)
            continue
        if x % 2 == 0:
            if cy != 0 and cx % 2 == 1:
                ans += 'L' * cy
                ans += 'D'
                cx += 1
                cy = 0
            elif cx % 2 == 1:
                ans += 'D'
                cx += 1
            ans += 'R' * (y-cy)
            cy = y
        else:
            if cy != 19 and cx % 2 == 0:
                ans += 'R' * (19-cy)
                ans += 'D'
                cx += 1
                cy = 19
            elif cx % 2 == 0:
                ans += 'D'
                cx += 1
            ans += 'L' * (cy-y)
            cy = y
        ans += 'I'
        yamafuda.append(no)

    cx += 1

    ans_list = [[-1] * 20 for i in range(5)]
    for x, y, no in haichi_list:
        ans_list[x-15][y] = no

    yamafuda = yamafuda[::-1]

    ans_a = 'D'

    # 配置フェーズ
    for i in range(20):
        if i % 2 == 0:
            for j in range(5):
                if j == 0:
                    if i != 0:
                        ans_a += 'L'
                else:
                    ans_a += 'D'
                if ans_list[j][19-i] != -1:
                    continue
                no = yamafuda.pop(0)
                ans_list[j][19-i] = no
                ans_a += 'O'
        else:
            for j in reversed(range(5)):
                if j == 4:
                    ans_a += 'L'
                else:
                    ans_a += 'U'
                if ans_list[j][19-i] != -1:
                    continue
                no = yamafuda.pop(0)
                ans_list[j][19-i] = no
                ans_a += 'O'

    # for i in range(5):
    #     print(ans_list[i])

    ans += ans_a

    haichi_list = []
    for i in range(5):
        for j in range(20):
            tmp = [i, j, ans_list[i][j]]
            haichi_list.append(tmp)

    haichi_list = sorted(haichi_list, key=lambda x: x[2])

    cx, cy = 0, 0

    for x, y, no in haichi_list:
        if cx <= x:
            ans += 'D' * (x-cx)
        else:
            ans += 'U' * (cx-x)
        if cy <= y:
            ans += 'R' * (y-cy)
        else:
            ans += 'L' * (cy-y)
        ans += 'I'
        cx, cy = x, y
    
    print(ans)


if __name__ == '__main__':
    main()
