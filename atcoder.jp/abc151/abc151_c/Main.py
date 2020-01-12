def main():
    N, M = map(int, input().split())

    ac_count = 0
    wa_count = 0

    if M == 0:
        print('{} {}'.format(ac_count, wa_count))
        exit()

    result_list = []

    for i in range(N):
        result_list.append([i+1, 0, 0])

    for i in range(M):
        str_list = input().split()
        if result_list[int(str_list[0])-1][1] == 1:
            continue
        if str_list[1] == 'AC':
            result_list[int(str_list[0])-1][1] = 1
        if str_list[1] == 'WA' and result_list[int(str_list[0])-1][1] == 0:
            result_list[int(str_list[0])-1][2] += 1

    for i in range(N):
        if result_list[i][1] == 1:
            ac_count +=1
            wa_count += result_list[i][2]

    print('{} {}'.format(ac_count, wa_count))

if __name__ == '__main__':
    main()