def main():
    h = int(input())
    w = int(input())
    n = int(input())

    if h >= w:
        big = h
    else:
        big = w

    if n <= big:
        print(1)
        exit()

    for i in range(big+1):
        if i * big >= n:
            count = i
            print(count)
            exit()
 
if __name__ == '__main__':
    main()