def main():
    n = int(input())

    for i in reversed(range(1,n+1)):
        if (i ** 0.5).is_integer():
            print(i)
            exit()

if __name__ == '__main__':
    main()