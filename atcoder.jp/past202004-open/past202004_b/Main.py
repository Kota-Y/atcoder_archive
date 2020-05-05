def main():
    s = input()

    a = 0
    b = 0
    c = 0
    d = 0

    for i in range(len(s)):
        if s[i] == 'a':
            a += 1
        elif s[i] == 'b':
            b += 1
        elif s[i] == 'c':
            c += 1
        elif s[i] == 'd':
            d += 1

    if a > b and a > c and a > d:
        print('a')
    if b > a and b > c and b > d:
        print('b')
    if c > a and c > b and c > d:
        print('c')
    if d > a and d > b and d > c:
        print('d')

if __name__ == '__main__':
    main()