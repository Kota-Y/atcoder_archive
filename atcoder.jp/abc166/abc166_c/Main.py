def main():
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    m_list = []
    for _ in range(m):
        m_list.append(list(map(int,input().split())))

    good_num = n

    list2 = [[] * 1 for i in range(n)]

    for i in range(m):
        list2[m_list[i][0]-1].append(m_list[i][1])
        list2[m_list[i][1]-1].append(m_list[i][0])

    for i in range(n):
        for j in range(len(list2[i])):
            if num_list[i] <= num_list[list2[i][j]-1]:
                good_num -= 1
                break

    print(good_num)

if __name__ == '__main__':
    main()