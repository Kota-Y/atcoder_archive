import numpy as np

def drop_process(drop_width, w_list, panel_array, num_list, num_point):
    print(drop_width)
    panel_array[w_list[drop_width]][drop_width] = num_list[num_point][0]    
    w_list[drop_width] += 1

def main():
    n, w, k, v = map(int, input().split())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    max_high = n // w # 段を埋められるMAXの高さ(125段)

    w_list = [0] * w # 各列のブロック数を初期化

    h_list = [-1] * max_high

    # k_list = [0] * k
    # for i in range(n):
    #     k_list[num_list[i][0]] += 1
    # print(k_list)

    panel_array = np.full((max_high, w), -1)

    drop_width = 0
    drop_process(drop_width, w_list, panel_array, num_list, 0)
    h_list[0] = num_list[0][0]

    for i in range(1,n):
        select_point = []
        # before_tmp = -1
        for j in range(w):
            tmp = [w_list[j], j]
            # if before_tmp == tmp[0]:
            #     break
            select_point.append(tmp)
            # before_tmp = tmp[0]

        flag = False
        for j in range(1,w):
            if w_list[j] >= 125:
                    continue
            if panel_array[select_point[j][0]][select_point[j][1]-1] == num_list[i][0]:
                drop_width = j
                flag = True
                break

        if not flag: 
            drop_width = w_list.index(max(w_list))

        if w_list[drop_width] >= 125:
            for o in range(w):
                if w_list[o] != 125:
                    drop_width = o
                    break

        drop_process(drop_width, w_list, panel_array, num_list, i)

    # print(panel_array)

if __name__ == '__main__':
    main()