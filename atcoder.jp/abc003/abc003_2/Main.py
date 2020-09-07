def main():
    s = input()
    t = input()

    atcoder = 'atcoder@'

    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] == '@' and t[i] in atcoder:
                continue
            if t[i] == '@' and s[i] in atcoder:
                continue
            print('You will lose')
            exit()

    print('You can win')

if __name__ == '__main__':
    main()
