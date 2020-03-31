def main():
    n = int(input())
    
    a_list = [n]

    for i in range(1000001):
        if a_list[i] % 2 == 0:
            tmp = a_list[i] // 2
        else:
            tmp = a_list[i] * 3 + 1
        
        if tmp in a_list:
            break
        a_list.append(tmp)

    print(len(a_list)+1)

if __name__ == '__main__':
    main()