def main():
    a, b, c = map(int, input().split())

    print(min(a+b,b+c,a+c))

if __name__ == '__main__':
    main()