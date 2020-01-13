def main():
    N = int(input())
    S, T = input().split()

    result = ''
    s_list = list(S)
    t_list = list(T)

    for i in range(N):
        result += s_list[i]
        result += t_list[i]


    print(result)

if __name__ == '__main__':
    main()