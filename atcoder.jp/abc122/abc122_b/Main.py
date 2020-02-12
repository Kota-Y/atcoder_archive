def main():
    s = input()

    ok_str = ['A', 'T', 'C', 'G']

    count = 0
    tmp = 0

    for i in range(len(s)):
        if s[i] in ok_str:
            tmp += 1
        else:
            if count < tmp:
                count = tmp
            tmp = 0

    if count < tmp:
        count = tmp

    print(count)

if __name__ == '__main__':
    main()