def i_input(): return int(input())

def main():
    n = i_input()

    ans_list = [0,0,1]

    if n <= 3:
        print(ans_list[n-1])
        exit()

    for i in range(3,n):
        ans_list.append(ans_list[i-3]%10007+ans_list[i-2]%10007+ans_list[i-1]%10007)

    print(ans_list[n-1]%10007)

if __name__ == '__main__':
    main()
