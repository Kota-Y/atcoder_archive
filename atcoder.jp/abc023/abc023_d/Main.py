import math

def main():
    n = int(input())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    right = 0
    left = 0

    for i in range(n):
        right = max(right, num_list[i][0] + num_list[i][1] * (n-1))
        left = max(left, num_list[i][0])

    while left <=  right:
        middle = (left+right) // 2
        tmp_list = []
        for i in range(n):
            tmp_list.append(math.ceil((middle - num_list[i][0]) // num_list[i][1]))
        else:
            tmp_list.sort()
            for i in range(n):
                if i > tmp_list[i]:
                    is_ok = False
                    left = middle + 1
                    break
            else:
                is_ok = True    
                right = middle - 1
        
    if is_ok:
        print(middle)
    else:
        print(middle+1)

if __name__ == '__main__':
    main()
