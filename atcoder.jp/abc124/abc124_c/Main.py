def main():
    s = input()

    ans1 = 0
    ans0 = 0

    s_len = len(s)

    for i in range(s_len):
        if i % 2 == 0:
            if s[i] == '0':
                ans1 += 1
        else:
            if s[i] == '1':
                ans1 += 1
            
    for i in range(s_len):
        if i % 2 == 0:
            if s[i] == '1':
                ans0 += 1
        else:
            if s[i] == '0':
                ans0 += 1

    print(min(ans0,ans1))

if __name__ == '__main__':
    main()