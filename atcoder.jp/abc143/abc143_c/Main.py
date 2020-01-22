def main():
    n = int(input())
    s = input()

    ls = [s[0]]

    index = 1

    while(n -1 >= index):
        if ls[len(ls)-1] != s[index]:
            ls.append(s[index])
        index += 1

    print(len(ls))

if __name__ == '__main__':
    main()