def main():
    n, m = map(int, input().split())

    if m >= n:
        print('unsafe')
    else:
        print('safe')

if __name__ == '__main__':
    main()