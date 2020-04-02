def main():
    n = int(input())
    str_list = []
    for _ in range(n):
        str_list.append(list(input().split()))
        
    money_sum = 0
    for i in range(n):
        if str_list[i][1] == 'JPY':
            money_sum += int(str_list[i][0])
        else:
            money_sum += 380000 * float(str_list[i][0])

    print(money_sum)      

if __name__ == '__main__':
    main()