def main():
    N = int(input())
    num_list = [int(input()) for _ in range(N)]
    
    print(len(set(num_list)))

if __name__ == '__main__':
    main()