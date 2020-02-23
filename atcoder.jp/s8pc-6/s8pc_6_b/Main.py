def main():
    n = int(input())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    ans = 0

    input_list = []
    output_list = []

    for i in range(n):
        input_list.append(num_list[i][0])
        output_list.append(num_list[i][1])

    input_list.sort()
    output_list.sort()

    input_num = input_list[n//2]
    output_num = output_list[n//2]

    for i in range(n):
        ans += abs(input_num - num_list[i][0])
        ans += num_list[i][1] - num_list[i][0]
        ans += abs(output_num - num_list[i][1])

    print(ans)

if __name__ == '__main__':
    main()