def main():
    s = list(input())

    s[3] = 8

    s = [str(i) for i in s]

    print(''.join(s))

if __name__ == '__main__':
    main()