def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))

    count = 0
    before = -1

    for i in range(n):
        count += b_list[a_list[i]-1]
        if before + 1 == a_list[i]:
            count += c_list[a_list[i]-2]
        before = a_list[i]

    print(count)

if __name__ == '__main__':
    main()