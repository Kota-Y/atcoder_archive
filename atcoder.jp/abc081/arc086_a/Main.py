from collections import Counter # 重複個数のカウント: Counter(num_list)

def main():
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))

    count_list = Counter(num_list)

    tmp_list = []

    for v in count_list.values():
        tmp_list.append(v)

    tmp_list.sort()
    
    count = 0
    for i in range(len(tmp_list)-k):
        count += tmp_list[i]

    print(count)

if __name__ == '__main__':
    main()