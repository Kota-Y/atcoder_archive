def main():
    s = input()
    k = int(input())

    if s[0] != '1':
        print(s[0])
        exit()

    for i in range(1,len(s)):
        if s[i] != '1':
            break
    else:
        print(1)
        exit()

    if i >= k:
        print(1)
        exit()

    print(s[i])

if __name__ == '__main__':
    main()