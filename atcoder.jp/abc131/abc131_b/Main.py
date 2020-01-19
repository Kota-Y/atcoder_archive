def main():
    n,l = map(int,input().split())

    aji_list = [0]*n

    count = 0

    for i in range(n):
        aji_list[i] = l + i

    if aji_list[0] >= 0:
        for i in range(1,n):
            count += aji_list[i]
    else:
        if aji_list[n-1] >= 0:
            for i in range(n):
                count += aji_list[i]
        else:
            for i in range(n-1):
                count += aji_list[i]

    print(count)

if __name__ == '__main__':
    main()