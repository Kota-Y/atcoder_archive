def main():
    n, m = map(int, input().split())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    # for i in range(n):
    #     print(num_list[i])

    # current_color = 'red'

    for i in range(m):
        if i % 4 == 0: # 赤色
            x = 0
            y = 0
            way = 'R'
            print(x,y,way)
        elif i % 4 == 1: # 青色
            x = 0
            y = n - 1
            way = 'D'
            print(x,y,way)
        elif i % 4 == 2: # 緑色
            x = n - 1
            y = 0
            way = 'U'
            print(x,y,way)
        elif i % 4 == 3: # 黄色
            x = n - 1
            y = n - 1
            way = 'L'
            print(x,y,way)
        
if __name__ == '__main__':
    main()