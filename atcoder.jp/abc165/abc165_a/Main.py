def main():
    n = int(input())
    a, b = map(int, input().split())

    for i in range(a,b+1):
        if i % n == 0:
            print('OK')
            exit()

    print('NG')

if __name__ == '__main__':
    main()