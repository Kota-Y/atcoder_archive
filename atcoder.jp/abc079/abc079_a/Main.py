def main():
    n = int(input())

    sn = str(n)

    if sn[1] == sn[2]:
        if sn[0] == sn[1] or sn[1] == sn[3]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()