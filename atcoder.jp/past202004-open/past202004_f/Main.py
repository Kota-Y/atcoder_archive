from heapq import heapify, heappop, heappush

def main():
    n = int(input())
    
    tmp_list = [[] for i in range(n)]    
    for _ in range(n):
        a, b = map(int, input().split())
        tmp_list[a-1].append(b)

    heapq = []
    point = 0

    for i in range(n):
        for j in tmp_list[i]:
            heappush(heapq, j * -1)
        point += heappop(heapq) * -1
        print(point)
        
if __name__ == '__main__':
    main()