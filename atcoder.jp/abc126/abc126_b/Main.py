def main():
    s = int(input())

    s1 = s // 100
    s2 = s - s1 * 100

    if s1 == 0:
        s1 = 13
    if s2 == 0:
        s2 = 13

    if s1 <= 12 and s2 <= 12:
        print('AMBIGUOUS')
    elif s1 <= 12 and s2 > 12:
        print('MMYY')
    elif s1 > 12 and s2 <= 12:
        print('YYMM')
    else:
        print('NA')

if __name__ == '__main__':
    main()