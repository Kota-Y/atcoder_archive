def main():
    s = input()

    count = 0

    sl = s.split('+')

    for l in sl:
        if l.find('0') == -1:
            count += 1

    print(count)

if __name__ == '__main__':
    main()