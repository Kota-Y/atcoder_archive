def main():
    a, b = map(int, input().split())

    if a < 10 and b < 10:
        print(a*b)
    else:
        print(-1)

if __name__ == '__main__':
    main()