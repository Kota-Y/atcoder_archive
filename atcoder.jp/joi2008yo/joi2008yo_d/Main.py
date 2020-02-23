def main():
    m = int(input())
    m_list = []
    for _ in range(m):
        m_list.append(list(map(int,input().split())))
    n = int(input())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    pin_x , pin_y = m_list[0][0], m_list[0][1]

    for i in range(n):
        move_x = num_list[i][0] - pin_x
        move_y = num_list[i][1] - pin_y
        for j in range(1,m):
            tmp_x = m_list[j][0] + move_x
            tmp_y = m_list[j][1] + move_y
            for k in range(n):
                if tmp_x == num_list[k][0] and tmp_y == num_list[k][1]:
                    break
            else:
                break
        else:
            print(move_x, move_y)

if __name__ == '__main__':
    main()