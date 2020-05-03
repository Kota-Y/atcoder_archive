def main():
    n, k = map(int, input().split())
    ans_list = []
    for i in range(k):
        d = int(input())
        num_list = list(map(int, input().split()))
        for j in range(d):
            ans_list.append(num_list[j])

    ans_list = list(set(ans_list))

    print(n - len(ans_list))

if __name__ == '__main__':
    main()