def s_input(): return input()

def uruu(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False

def main():
    s = s_input()

    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:])

    uruu_flag = uruu(y)

    remove = [4, 6, 9, 11]

    for i in range(m, 13):
        for j in range(1, 32):
            if i in remove and j == 31:
                continue
            if i == 2 and j > 28:
                if uruu_flag and j == 29:
                    pass
                else:
                    continue
            if (y / i / j).is_integer():
                if i == m and j < d:
                    continue
                if len(str(i)) == 1:
                    i = '0' + str(i)
                if len(str(j)) == 1:
                    j = '0' + str(j)
                print(y, end='')
                print('/', end='')
                print(i, end='')
                print('/', end='')
                print(j)
                exit()

    print(y+1, end='')
    print('/01/01')

if __name__ == '__main__':
    main()
