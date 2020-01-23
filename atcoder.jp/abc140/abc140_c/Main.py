def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    
    ls = [num_list[0]]

    for i in range(n-1):
        if i != n - 2 and num_list[i+1] < num_list[i]:
            ls.append(num_list[i+1])
        else:
            ls.append(num_list[i])

    print(sum(ls))

if __name__ == '__main__':
    main()