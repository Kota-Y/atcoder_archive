def main():
    s = input()

    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])

    for i in range(2):
        tmp = 0
        if i % 2 == 0:
            tmp = a + b 
        else:
            tmp = a - b
        for j in range(2):
            if j % 2 == 0:
                hoge1 = tmp
                tmp += c
            else:
                tmp = hoge1
                tmp -= c
            for k in range(2):
                if k % 2 == 0:
                    hoge = tmp
                    tmp += d
                else:
                    tmp = hoge
                    tmp -= d
                if tmp == 7:
                    op1 = '+' if i % 2 == 0 else '-'
                    op2 = '+' if j % 2 == 0 else '-'
                    op3 = '+' if k % 2 == 0 else '-'
                    print(str(a)+op1+str(b)+op2+str(c)+op3+str(d)+'=7')
                    exit()
            

    # print(i,j,k,tmp)

if __name__ == '__main__':
    main()