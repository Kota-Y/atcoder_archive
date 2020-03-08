def main():
    s = input()

    sc = s.count('h')
    sh = s.count('i')

    if sc != sh:
        print('No')
        exit()

    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != 'h':
                break
        else:
            if s[i] != 'i':
                break
    else:
        print('Yes')
        exit()

    print('No')

if __name__ == '__main__':
    main()