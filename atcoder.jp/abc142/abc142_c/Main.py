def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    
    ls = [0] * n

    for i in range(n):
        ls[num_list[i]-1] = i + 1

    print(*ls)

if __name__ == '__main__':
    main()