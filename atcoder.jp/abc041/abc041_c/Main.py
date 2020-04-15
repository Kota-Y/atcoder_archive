def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    heiht_list = []
    for i in range(n):
        tmp_list = [num_list[i], i+1]
        heiht_list.append(tmp_list)

    heiht_list.sort(reverse = True)

    for i in range(n):
        print(heiht_list[i][1])

if __name__ == '__main__':
    main()