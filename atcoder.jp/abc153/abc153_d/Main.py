def main():
    h = int(input())

    i = 0

    while(h >= 1):
        h //= 2
        i += 1

    print(2**i-1)

if __name__ == '__main__':
    main()