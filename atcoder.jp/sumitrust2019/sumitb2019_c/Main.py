def main():
    x = int(input())

    tmp = x // 100

    x = x - tmp * 100

    if x <= tmp * 5:
        print('1')
    else:
        print('0')

if __name__ == '__main__':
    main()
