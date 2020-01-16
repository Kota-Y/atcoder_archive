def main():
    s = input()
    t = input()

    count = 0

    for i in range(3):
        if s[i-1] == t[i-1]:
            count +=1

    print(count)

if __name__ == '__main__':
    main()