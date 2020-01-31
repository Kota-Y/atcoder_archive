def main():
    n = int(input())
    str_list = []
    for i in range(n):
        str_list.append(list(input().split() + [i+1]))

    str_list = sorted(str_list, key = lambda x:(x[0], -int(x[1])))

    for i in range(n):
        print(str_list[i][2])

if __name__ == '__main__':
    main()