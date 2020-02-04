def main():
    n, k = map(int, input().split())
    s = list(input())

    s[k-1] = s[k-1].lower()

    print(''.join(s))

if __name__ == '__main__':
    main()