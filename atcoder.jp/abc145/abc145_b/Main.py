def main():
    n = int(input())
    s = input()

    if len(s) % 2 != 0:
        print('No')
        exit()

    for i in range(len(s)//2):
        if s[i] != s[i+len(s)//2]:
            print('No')
            exit()

    print('Yes')

if __name__ == '__main__':
    main()