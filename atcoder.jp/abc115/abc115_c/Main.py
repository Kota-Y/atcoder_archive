def main():
    n, k = map(int, input().split())
    num_list = []
    for _ in range(n):
        num_list.append(int(input()))
    
    num_list.sort()

    min_count = 10**9
    for i in range(n-k+1):
        min_count = min(min_count, num_list[k-1+i]-num_list[i])

    print(min_count)

if __name__ == '__main__':
    main()