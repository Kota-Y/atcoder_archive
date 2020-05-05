def main():
    s, t = input().split()

    flag = False

    if s[0] == 'B':
        si = int(s[1]) * -1
        flag = not flag
    else:
        si = int(s[0])

    if t[0] == 'B':
        ti = int(t[1]) * -1
        flag = not flag
    else:
        ti = int(t[0])

    if flag:
        print(abs(ti-si)-1)
    else:
        print(abs(ti-si))

if __name__ == '__main__':
    main()