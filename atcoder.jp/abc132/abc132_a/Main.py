def main():
    s = input()

    sl = list(s)

    ss = set(sl)

    if len(ss) != 2:
        print('No')
        exit()

    if sl.count(list(ss)[0]) != 2:
        print('No')
        exit()

    print('Yes')

 
if __name__ == '__main__':
    main()