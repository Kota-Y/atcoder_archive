def main():
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum_count = 0
    for i in range(m):
        sum_count += num_list[i]

    print(n-sum_count if n >= sum_count else -1)

if __name__ == '__main__':
    main()