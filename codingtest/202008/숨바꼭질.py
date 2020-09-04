import sys
from collections import deque
sys.stdin=open("in.txt", "r")
q = deque()
def BFS(cur):
    ch[cur]=1
    q.append((cur, 1))

    while q:
        tmp = q.popleft()
        #현재위치
        tc = tmp[0]
        #현재시간
        tt = tmp[1]
        #앞으로 한번 갈 때(+1), 뒤로 한번 갈 때(-1), 순간이동 할 때(*2)
        dt = [1, -1, tc]

        for i in range(3):
            x = tc+dt[i]
            if x == k:
                print(tmp[1])
                return
            #갈 수 있는 범위, 만약 갈 수 있는 곳이라면
            if 0<=x<=200002:
                #그리고 방문하지 않은 곳이라면
                if ch[x]==0:
                    #방문하고, 큐에 넣는다(시간은 1초 지남)
                    ch[x]=1
                    q.append((x, tt+1))



if __name__=="__main__":
    n, k = map(int, input().split())
    #같은 지점에 있었을 때
    if k==n:
        print(0)
        sys.exit(0)

    #방문 체크
    ch = [0]*200003

    BFS(n)

