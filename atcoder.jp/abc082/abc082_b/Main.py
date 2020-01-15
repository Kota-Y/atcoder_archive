def main():
    s = input()
    t = input()

    s = list(s)
    t = list(t)

    s = sorted(s)
    t = sorted(t, reverse=True)

    if s < t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()