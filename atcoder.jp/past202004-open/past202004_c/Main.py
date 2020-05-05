def main():
    n = int(input())
    str_list = []
    for _ in range(n):
        str_list.append(list(input().split()))

    for i in reversed(range(n-1)):
        for j in range(1,2*n-2):
            if str_list[i][0][j] == '.':
                continue
            if str_list[i+1][0][j-1] == 'X' or str_list[i+1][0][j] == 'X' or str_list[i+1][0][j+1] == 'X':
                tmp_str = ''
                for s in range(2*n-1):
                    if s == j:
                        tmp_str = tmp_str + 'X'                  
                    else:
                        tmp_str = tmp_str + str_list[i][0][s]
                str_list[i] = [tmp_str]
            
    for i in range(n): 
        print((str_list)[i][0])
    

if __name__ == '__main__':
    main()