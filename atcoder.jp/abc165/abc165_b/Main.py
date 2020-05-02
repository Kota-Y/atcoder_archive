import math

def main():
    x = int(input())

    start_num = 100
    max_num = 3760+1000
    for i in range(max_num):
        if start_num >= x:
            print(i)
            exit()
        start_num = start_num + math.floor(start_num * 0.01)

if __name__ == '__main__':
    main()