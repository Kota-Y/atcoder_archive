def main():
    s = input()

    if s[0] != 'A':
        print('WA')
        exit()
    
    if s[2:-1].count('C') != 1:
        print('WA')
        exit()  

    s = s[1:]
    s = s.replace('C','')

    if not s.islower():
        print('WA')
        exit()  

    print('AC')

if __name__ == '__main__':
    main()