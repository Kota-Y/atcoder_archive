def main():
    n, x = map(int, input().split())
    num_list = [int(input()) for _ in range(n)]

    ans = n

    min_sum = sum(num_list)

    while x - min_sum >= 0:
        x -= min(num_list)
        ans += 1

    print(ans-1)

if __name__ == '__main__':
    main()