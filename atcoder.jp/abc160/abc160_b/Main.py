def main():
    x = int(input())

    y500 = x // 500
    y5 = (x - (y500*500)) // 5

    print(1000*y500+5*y5)

if __name__ == '__main__':
    main()