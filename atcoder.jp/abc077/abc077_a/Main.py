def main():
    s1 = input()
    s2 = input()

    s2 = s2[::-1]

    print('YES' if s1 == s2 else 'NO')

if __name__ == '__main__':
    main()