def main():
    s = input()

    before = s[0:(len(s)-1)//2]
    after = s[(len(s)+3)//2-1:len(s)]

    print('Yes' if before == after else 'No')

if __name__ == '__main__':
    main()