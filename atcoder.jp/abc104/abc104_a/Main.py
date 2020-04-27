def main():
    n = int(input())

    if n >= 2800:
        print('AGC')
    elif n >= 1200:
        print('ARC')
    else:
        print('ABC')

if __name__ == '__main__':
    main()