def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    ans_list = []
    for i in range(n):
        count = 1
        index = i
        while True:
            if i + 1 == num_list[index]:
                ans_list.append(count)
                break
            index = num_list[index] - 1
            count += 1
    
    print(' '.join(map(str, ans_list)))

if __name__ == '__main__':
    main()