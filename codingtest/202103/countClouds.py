from collections import deque
def BFS(x, y, skyMap):
    n = len(skyMap)
    m = len(skyMap[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and skyMap[nx][ny] == '1':
                skyMap[nx][ny] = '0'
                q.append((nx, ny))

    return skyMap


def countClouds(skyMap):
    cnt = 0
    if not skyMap:
        return 0
    n = len(skyMap)
    m = len(skyMap[0])
    for i in range(n):
        for j in range(m):
            if skyMap[i][j] == '1':
                skyMap = BFS(i, j, skyMap)
                cnt+=1
    return cnt





if __name__ == "__main__":
    print(countClouds([['0', '1', '1', '0', '1'],
          ['0', '1', '1', '1', '1'],
          ['0', '0', '0', '0', '1'],
          ['1', '0', '0', '1', '1']]))
