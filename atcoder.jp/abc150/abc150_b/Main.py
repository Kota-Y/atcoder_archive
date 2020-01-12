def main():
    N = int(input())
    S = input()

    S = S.replace('ABC','-')

    print(S.count('-'))

if __name__ == '__main__':
    main()