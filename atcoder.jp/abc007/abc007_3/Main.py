from collections import deque

inf = 10 ** 9

def bfs(si, sj, str_list, dist, h, w):
    q = deque([[si, sj]])
    dist[si][sj] = 0
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
    return dist

def main():
    r, c = map(int, input().split())
    si, sj = map(int, input().split())
    gi, gj = map(int, input().split())
    str_list = []
    for _ in range(r):
        str_list.append(list(input().split()))

    dist = [[inf] * c for i in range(r)]

    dist_result = bfs(si-1, sj-1, str_list, dist, r, c)

    print(dist_result[gi-1][gj-1])

if __name__ == '__main__':
    main()