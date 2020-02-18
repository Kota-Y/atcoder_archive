from collections import Counter # 重複個数のカウント: Counter(num_list)

def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    ans = 0

    count_dict = Counter(num_list)

    for k, v in count_dict.items():
        if k == v:
            continue
        if k < v:
            ans += v - k
        else:
            ans += v
            
    print(ans)

if __name__ == '__main__':
    main()