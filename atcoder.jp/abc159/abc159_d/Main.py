from collections import Counter # 重複個数のカウント: Counter(num_list)

def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    ans_list = [0] * n
    cnt_list = Counter(num_list)
    for k, v in cnt_list.items():
        if v == 1:
            ans_list[k-1] = 0
            continue
        ans_list[k-1] = v * (v-1) // 2
        
    sum_num = sum(ans_list)

    ans = sum_num

    for i in range(n):
        ans -= ans_list[num_list[i]-1]
        if cnt_list[num_list[i]]-1 != 1:
            ans += (cnt_list[num_list[i]]-1) * (cnt_list[num_list[i]]-2) // 2
        print(ans)
        ans = sum_num

if __name__ == '__main__':
    main()