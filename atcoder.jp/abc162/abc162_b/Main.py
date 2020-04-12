def main():
    n = int(input())

    sum_count = 0

    for i in range(1,n+1):
        if i % 3 == 0:
            continue
        if i % 5 == 0:
            continue
        sum_count += i

    print(sum_count)

if __name__ == '__main__':
    main()