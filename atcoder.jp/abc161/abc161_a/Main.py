def main():
    a, b, c = map(int, input().split())

    a, b = b, a
    a, c = c, a

    print(a,b,c)

if __name__ == '__main__':
    main()