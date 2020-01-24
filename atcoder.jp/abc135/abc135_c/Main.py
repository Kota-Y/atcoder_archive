def main():
    n = int(input())
    machi_list = list(map(int, input().split()))
    yusha_list = list(map(int, input().split()))

    init_sum = sum(machi_list)

    for i in range(n):
        machi_list[i] -= yusha_list[i]
        if machi_list[i] < 0:
            machi_list[i+1] += machi_list[i]
            if machi_list[i+1] < 0:
                machi_list[i+1] = 0
            machi_list[i] = 0

    print(init_sum-sum(machi_list))

if __name__ == '__main__':
    main()