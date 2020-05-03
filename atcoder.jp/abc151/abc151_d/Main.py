from collections import deque

inf = 10 ** 9

def bfs(si, sj, str_list, dist, h, w):
    q = deque([[si, sj]])
    dist[si][sj] = 0
    max_tmp = 0
    while len(q) != 0:
        i, j = q.popleft()
        for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ni = i + dx
            nj = j + dy
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if str_list[ni][0][nj] != '.':
                continue
            if dist[ni][nj] != inf:
                continue
            dist[ni][nj] = dist[i][j] + 1
            q.append([ni, nj])
            max_tmp = max(max_tmp, dist[ni][nj])
    return max_tmp

def main():
    h, w = map(int, input().split())
    str_list = []
    for i in range(h):
        str_list.append(list(input().split()))

    max_num = 0

    for si in range(h):
        for sj in range(w):
            if str_list[si][0][sj] != '.':
                continue
            dist = [[inf] * w for i in range(h)]
            bfs_result = bfs(si, sj, str_list, dist, h, w)
            max_num = max(max_num, bfs_result)

    print(max_num)  

if __name__ == '__main__':
    main()