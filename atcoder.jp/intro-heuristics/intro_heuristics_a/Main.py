import sys
from copy import deepcopy
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row_list(N): return [i_list() for _ in range(N)]
sys.setrecursionlimit(10 ** 6)
INF = float('inf')

def main():
    d = i_input()
    c_list = i_list()
    s_list = i_row_list(d)

    output_list = []

    last_list = [0] * 26

    for day in range(1,d+1):
        result = 0
        max_point = -INF
        for i in range(26):
            plus_point = s_list[day-1][i]
            minus_point = 0
            for j in range(26):
                if i == j:
                    continue
                minus_point += c_list[j] * (day - last_list[j])
            sum_point = plus_point - minus_point

            if day != d:
                last_list2 = deepcopy(last_list)
                last_list2[i] = day
                result2 = 0
                max_point2 = -INF
                for k in range(26):
                    plus_point2 = s_list[day][k]
                    minus_point2 = 0
                    for h in range(26):
                        if k == h:
                            continue
                        minus_point2 = c_list[h] * (day+1 - last_list2[h])
                    sum_point2 = plus_point2 - minus_point2

                    if day != d-1:
                        last_list3 = deepcopy(last_list2)
                        last_list3[k] = day + 1
                        result3 = 0
                        max_point3 = -INF
                        for l in range(12):
                            plus_point3 = s_list[day+1][l]
                            minus_point3 = 0
                            for m in range(26):
                                if l == m:
                                    continue
                                minus_point3 = c_list[m] * (day+2 - last_list3[m])
                            sum_point3 = plus_point3 - minus_point3
                        if sum_point3 > max_point3:
                            result3 = l + 1
                            max_point3 = sum_point3
                        last_list3[result3-1] = day + 2
                    else:
                        max_point3 = 0

                    if sum_point2 + max_point3 > max_point2:
                        result2 = k + 1
                        max_point2 = sum_point2 + max_point3
                    last_list2[result2-1] = day + 1
            else:
                max_point2 = 0

            if sum_point + max_point2 > max_point:
                result = i + 1
                max_point = sum_point + max_point2
        output_list.append(result)
        last_list[result-1] = day

    for out in output_list:
        print(out)

if __name__ == '__main__':
    main()
