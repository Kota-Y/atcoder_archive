def main():
    a,b,c = map(int, input().split())

    x = a - b - c

    if 0 >= x:
        print(abs(x))
    else:
        print(0)
    

if __name__ == '__main__':
    main()