def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    ans = 0

    num_list = [a,b,c,d,e]

    min_num = 10
    for i in num_list:
        if i % 10 < min_num and i % 10 != 0:
            min_num = i % 10
        if i % 10 == 0:
            ans += i
        else:
            ans += i + ( 10 - i % 10 )

    print(ans-10+min_num)

if __name__ == '__main__':
    main()