def digitNum(n):
    tmp = str(n)
    d = len(tmp)
    
    return d

def main():
    a,b,x = map(int, input().split())

    count = 0

    max = 10**9
    min = 0

    while(max - min > 1):
        mid = (max + min) // 2
        # print(a * mid + b * digitNum(mid),max,min,mid)
        if x >= a * mid + b * digitNum(mid):
            count = mid
            min = mid
            if min == 999999999:
                if x >= a * max + b * digitNum(max):
                    count = max

        else:
            max = mid

    
    print(count)

 
if __name__ == '__main__':
    main()