import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

def main():
    n = int(input())

    sum_count = 0
    for i in range(1,n+1):
        tmp_list = []
        tmp_list.append(i)
        for j in range(1,n+1):
            tmp_list.append(j)
            for k in range(1,n+1):
                tmp_list.append(k)              
                sum_count += gcd_list(tmp_list)
                tmp_list.pop(2)
            tmp_list.pop(1)

    print(sum_count)        

if __name__ == '__main__':
    main()