def main():
    n, m = map(int, input().split())

    num_list = []
    for _ in range(n): 
        num_list.append(list(map(int,input().split())))

    ans = 0

    ans_list = [0] * m

    for i in range(n):
        for j in range(num_list[i][0]):
            ans_list[num_list[i][j+1]-1] += 1
        
    for i in range(m):
        if n == ans_list[i]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()