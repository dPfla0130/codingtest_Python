import sys
from collections import deque

sys.stdin=open("in.txt", "r")

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def BFS(sx, sy, ss):
    q = deque()
    q.append((sx, sy, ss))
    ch[sx][sy]=1
    global e
    t = 0
    answer =0

    eat_flag = False
    while q:

        size = len(q)
        #위, 왼쪽을 더 우선시해서 가야하기 때문에, BFS queue를 정렬해준다
        q = deque(sorted(q))

        for _ in range(size):
            x, y, s = q.popleft()

            if 0< board[x][y] and board[x][y]<s:
                for i in range(n):
                    print(tboard[i])
                print()
                e += 1
                board[x][y]=0
                for i in range(n):
                    for j in range(n):
                        ch[i][j]=0

                while q:
                    q.popleft()

                #먹었을 때 시간 저장하기
                answer = t
                eat_flag = True
                #만약 먹은 개수가 같아지면 크기가 1증가한다
                if e==s:
                    s+=1
                    e=0


            for i in range(4):
                tx = x+dx[i]
                ty = y+dy[i]
                if 0<=tx<n and 0<=ty<n and ch[tx][ty]==0 and s>=board[tx][ty]:
                    ch[tx][ty]=1
                    tboard[tx][ty] = tboard[x][y]+1
                    q.append((tx, ty, s))
            if eat_flag:
                eat_flag = False
                break
        t+=1
    return answer

if __name__=="__main__":
    n = int(input())
    ch = [[0]*n for _ in range(n)]
    board = [list(map(int, input().split())) for _ in range(n)]
    tboard = [[0]*n for _ in range(n)]
    cnt=0
    e = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                x, y = i, board[i].index(9)
                board[x][y] = 0

    print(BFS(x, y, 2))
