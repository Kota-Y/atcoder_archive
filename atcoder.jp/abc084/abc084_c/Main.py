def main():
    n = int(input())
    num_list = []
    for _ in range(n-1):
        num_list.append(list(map(int,input().split())))

    for i in range(n):
        t = 0
        for j in range(i,n-1):
            if t <= num_list[j][1]:
                t = num_list[j][1]
            elif t % num_list[j][2] != 0:
                t = (t // num_list[j][2]+1) * num_list[j][2]
            t += num_list[j][0]
        print(t)

if __name__ == '__main__':
    main()