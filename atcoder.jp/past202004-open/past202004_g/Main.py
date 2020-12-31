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
    n = i_input()
    q = deque()

    for _ in range(n):
        tmp = s_list()
        if tmp[0] == '1':
            q.append([tmp[1], int(tmp[2])])
        else:
            if len(q) == 0:
                print(0)
                continue
            delete_num = int(tmp[1])
            pop_tmp = q.popleft()
            tmp_s = dict()
            while True:
                if delete_num <= pop_tmp[1]:
                    if pop_tmp[0] in tmp_s:
                        tmp_num = tmp_s[pop_tmp[0]]
                        tmp_s[pop_tmp[0]] = delete_num + tmp_num
                    else:
                        tmp_s[pop_tmp[0]] = delete_num
                    q.appendleft([pop_tmp[0], pop_tmp[1]-delete_num])
                    break
                elif delete_num > pop_tmp[1]:
                    delete_num -= pop_tmp[1]
                    if pop_tmp[0] in tmp_s:
                        tmp_num = tmp_s[pop_tmp[0]]
                        tmp_s[pop_tmp[0]] = pop_tmp[1] + tmp_num
                    else:
                        tmp_s[pop_tmp[0]] = pop_tmp[1]
                    if len(q) == 0:
                        break
                    pop_tmp = q.popleft()

            tmp_s_co = Counter(tmp_s)
            ans = 0
            for value in tmp_s_co.values():
                ans += pow(value, 2)
            print(ans)

if __name__ == '__main__':
    main()
