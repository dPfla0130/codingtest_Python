from collections import deque
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(m, n, office):
    while q:
        x, y, day = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #바이러스를 퍼트릴 수 있으면
            if 0 <= nx < m and 0 <= ny < n and office[nx][ny] == 0:
                #바이러스 퍼트린 날짜로 board를 업데이트 해준다
                office[nx][ny] = day+1
                q.append((nx, ny, day+1))
    #만약에 board에 0이 있으면 감염되지 않은 사람이 있는 것으로 -1 반환
    for i in range(len(office)):
        for j in range(len(office[i])):
            if office[i][j] == 0:
                return -1
    #만약에 바이러스를 퍼트리는데 걸린 날짜가 1이거나 -1면 모두 감염된 상태였거나, 백신을 맞은 상태
    #아니라면 날짜 반환
    lday = -1
    for i in range(len(office)):
        lday = max(max(office[i]), lday)
    if lday == 1 or lday == -1:
        return 0
    else:
        return lday-1

def solution(m, n, infests, vaccinateds):
    office = [[0]*n for _ in range(m)]
    for i in infests:
        office[i[0]-1][i[1]-1] = 1
        q.append((i[0]-1, i[1]-1, 1))
    for i in vaccinateds:
        office[i[0]-1][i[1]-1] = -1
    return BFS(m, n, office)

if __name__=="__main__":
    solution(m=2, n=4, infests=[[1,4],[2,2]], vaccinateds=[[1,2]])