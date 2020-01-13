def main():
    s = input()

    odd = 1
    even = 1

    for i in range(1,len(s)+1):
        if i % 2 == 0:
            if s[i-1] == 'R':
                odd = 0
        else:
            if s[i-1] == 'L':
                even = 0

    if odd == 1 and even == 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()