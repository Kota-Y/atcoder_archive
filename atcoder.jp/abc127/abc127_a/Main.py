def main():
    a, b = map(int, input().split())

    price = b

    if 6 <= a <= 12:
        price //= 2
    elif 5 >= a:
        price = 0

    print(price)

if __name__ == '__main__':
    main()