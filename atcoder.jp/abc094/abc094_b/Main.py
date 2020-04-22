def main():
    n, m, x = map(int, input().split())
    num_list = list(map(int, input().split()))

    low_count = 0
    high_count = 0
    for i in num_list:
        if i < x:
            low_count += 1
        elif i > x:
            high_count += 1

    print(min(low_count, high_count))

if __name__ == '__main__':
    main()