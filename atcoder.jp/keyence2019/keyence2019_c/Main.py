import numpy as np

def main():
    n = int(input())
    junbi_num = list(map(int, input().split()))
    exam_num = list(map(int, input().split()))

    min = -1

    if sum(junbi_num) < sum(exam_num):
        print(min)
        exit()

    sabun_list = np.array(junbi_num) - np.array(exam_num)

    min = np.count_nonzero(sabun_list < 0)
    
    plus_list = sabun_list[sabun_list > 0]
    plus_list = np.sort(plus_list)[::-1]

    minus = sum(sabun_list[sabun_list < 0])

    i = 0
    while(minus < 0):
        minus += plus_list[i]
        i += 1
        min += 1

    print(min)

if __name__ == '__main__':
    main()
