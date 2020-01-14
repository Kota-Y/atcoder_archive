def main():
    n = int(input())
    a = int(input())

    x = n % 500

    if x <= a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()