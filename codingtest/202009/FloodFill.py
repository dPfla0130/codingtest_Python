from collections import deque
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(sx, sy, n, m, image, chk):
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and chk[nx][ny] == 0:
                if image[nx][ny] == image[x][y]:

                    chk[nx][ny] = 1
                    q.append((nx, ny))


def solution(n, m, image):
    answer = 0
    chk = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if chk[i][j]==0:
                chk[i][j] = 1
                BFS(i, j, n, m, image, chk)
                answer+=1
    print(answer)

    return answer

if __name__=="__main__":
    n = 3
    m = 2
    image = [[1, 2], [1, 2], [4, 5]]
    solution(n, m, image)