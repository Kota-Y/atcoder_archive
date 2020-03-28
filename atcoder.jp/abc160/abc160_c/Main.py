def main():
    k, n = map(int, input().split())
    num_list = list(map(int, input().split()))

    num_list.append(k+num_list[0])

    tmp = 0
    for i in range(n):
        tmp = max(tmp, num_list[i+1]-num_list[i])

    print(k-tmp)

if __name__ == '__main__':
    main()