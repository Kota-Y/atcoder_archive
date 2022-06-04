from socket import IP_MULTICAST_LOOP
import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
def ceil(a, b): return (a + b - 1) // b
def floor(a, b): return a // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def create_graph(n: int, l: list) -> list:
    graph = [[] for _ in range(n+1)]
    for a, b in l:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def get_ans(x, k, graph):
    if k == 0:
        return x

    ans_set = set()
    ans_set.add(x)
    if k == 1:
        for node in graph[x]:
            ans_set.add(node)
        return sum(ans_set)

    if k == 2:
        first_nodes = []
        for node in graph[x]:
            ans_set.add(node)
            first_nodes.append(node)

        second_nodes = []
        for first_node in first_nodes:
            for node in graph[first_node]:
                if node in ans_set:
                    continue
                ans_set.add(node)
                second_nodes.append(node)

        return sum(ans_set)

    if k == 3:
        first_nodes = []
        for node in graph[x]:
            ans_set.add(node)
            first_nodes.append(node)

        second_nodes = []
        for first_node in first_nodes:
            for node in graph[first_node]:
                if node in ans_set:
                    continue
                ans_set.add(node)
                second_nodes.append(node)

        # third_nodes = []
        for second_node in second_nodes:
            for node in graph[second_node]:
                if node in ans_set:
                    continue
                ans_set.add(node)
                # third_nodes.append(node)

        return sum(ans_set)

def main():
    n, m = i_map()
    edges = i_row_list(m)

    graph = create_graph(n, edges)
    # print(graph)
    q = i_input()
    for _ in range(q):
        x, k = i_map()
        res = get_ans(x, k, graph)
        print(res)
        
if __name__ == '__main__':
    main()
