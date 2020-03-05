def main():
    n, k = map(int, input().split())

    print(1 if n%k!=0 else 0)

if __name__ == '__main__':
    main()