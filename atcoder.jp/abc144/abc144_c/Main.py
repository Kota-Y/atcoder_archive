def main():
    n = int(input())

    count = n + 1

    for i in range(1,int(n**0.5)+1):
        if n % i == 0 and n // i + i < count:
            count = n // i + i

    print(count-2)

if __name__ == '__main__':
    main()