def main():
    n = int(input())

    if n < 100:
        print('00')
    elif 100 <= n and n <= 5000:
        print('0' + str(n//100) if n < 1000 else n//100)
    elif 6000 <= n and n <= 30000:
        print(n//1000+50)
    elif 3500 <= n and n <= 70000:
        print((n//1000-30)//5+80)
    elif 70 < n:
        print(89)

if __name__ == '__main__':
    main()
