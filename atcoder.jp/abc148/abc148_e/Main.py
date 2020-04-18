def main():
    n = int(input())

    if n % 2 != 0:
        print(0)
        exit()

    zero_count = 0

    i = 10
    while n // i != 0:
        zero_count += n // i
        i *= 5

    print(zero_count)

if __name__ == '__main__':
    main()