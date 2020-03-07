def main():
    s = input()

    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            print('Yes')
            exit()

    print('No')
    
if __name__ == '__main__':
    main()