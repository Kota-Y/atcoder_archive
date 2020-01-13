def main():
    n = int(input())

    odd = 0

    for i in range(1,n+1):
        if i % 2 != 0:
            odd += 1

    print(odd/n)

if __name__ == '__main__':
    main()