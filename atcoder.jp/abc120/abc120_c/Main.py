def main():
    s = input()

    zero = s.count('0')
    one = len(s) - zero

    print(min(zero, one) * 2)

if __name__ == '__main__':
    main()