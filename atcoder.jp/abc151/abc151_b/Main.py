def main():
    N, K, M = map(int, input().split()) # N: 科目数, K: K点満点, M: 平均点
    num_list = list(map(int, input().split()))

    sum_score = 0
    goal_score = N * M

    for i in range(N-1):
        sum_score += num_list[i]

    need_score = goal_score - sum_score

    if need_score < 0:
        need_score = 0

    if need_score > K:
        print(-1)
    else:
        print(need_score)

if __name__ == '__main__':
    main()