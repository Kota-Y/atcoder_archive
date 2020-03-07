def main():
    h, w = map(int, input().split())
    str_list = []
    for _ in range(h):
        str_list.append(list(input().split()))

    for i in range(h):
        for j in range(w):
            if str_list[i][0][j] != '.':
                break
        else:
            for _ in range(w):
                str_list[i][0] = '!' * w
                
    delete_index_list = []

    for i in range(w):
        for j in range(h):
            if str_list[j][0][i] != '.' and str_list[j][0][i] != '!':
                break
        else:
            delete_index_list.append(i)

    for i in range(h):
        for j in range(w):
            if j in delete_index_list:
                continue
            if str_list[i][0][j] != '!':
                print(str_list[i][0][j], end='')
            else:
                break
        else:
            print()


if __name__ == '__main__':
    main()