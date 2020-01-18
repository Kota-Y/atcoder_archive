def main():
    s = input()

    good = 'keyence'

    for start in range(len(s)):
        for end in range(len(s)):
            if s.replace(s[start:end],'',1) == good:
                print('YES')
                exit()

    print('NO')

if __name__ == '__main__':
    main()
