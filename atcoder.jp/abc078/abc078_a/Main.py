def main():
    x, y = input().split()

    if x == y:
        print('=')
        exit()

    print('<' if x < y else '>')

if __name__ == '__main__':
    main()