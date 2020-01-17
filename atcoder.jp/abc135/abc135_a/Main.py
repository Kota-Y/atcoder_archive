def main():
    a,b = map(int,input().split())

    if (a+b) % 2 != 0:
        print('IMPOSSIBLE')
    else:
        print((a+b)//2)

if __name__ == '__main__':
    main()
