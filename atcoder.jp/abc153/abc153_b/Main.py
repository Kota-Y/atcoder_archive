def main():
    h, n = map(int, input().split())

    num_list = list(map(int, input().split()))

    isWin = False

    for num in num_list:
        h -= num
        if h <= 0:
            isWin = True
            break

    print('Yes' if isWin else 'No')

if __name__ == '__main__':
    main()