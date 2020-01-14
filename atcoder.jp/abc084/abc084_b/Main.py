def main():
    a,b = map(int, input().split())
    s = input()

    if s[a] != '-':
        print('No')
        exit()
    
    slist = list(s)
    slist[a] = ''

    if ''.join(slist).isdigit():
        print('Yes')
        exit()

    print('No')

if __name__ == '__main__':
    main()