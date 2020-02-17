def main():
    a, b, c = map(int, input().split())

    ans = b // a

    print(ans if ans < c else c)

if __name__ == '__main__':
    main()