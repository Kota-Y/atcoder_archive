def main():
    n = int(input())
    num_list = [int(input()) for _ in range(n)]

    light_no = 1
    for i in range(n):
        if light_no == 2:
            print(i)
            exit()
        light_no = num_list[light_no-1]
    
    print(-1)

if __name__ == '__main__':
    main()