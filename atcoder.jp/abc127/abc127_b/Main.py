def main():
    r, d, x= map(int, input().split())

    tmp = x

    for _ in range(10):
        tmp = r * tmp - d
        print(tmp)

if __name__ == '__main__':
    main()