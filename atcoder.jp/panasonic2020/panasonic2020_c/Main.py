def main():
    a, b, c = map(int, input().split())

    if c - a - b <= 0:
        print('No')
        exit()

    if 4 * a * b < pow(c - a - b, 2):
        is_big = True
    else:
        is_big = False

    print('Yes' if is_big else 'No')

if __name__ == '__main__':
    main()
