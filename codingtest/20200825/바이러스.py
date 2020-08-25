import sys

sys.stdin=open("in.txt", "r")
def DFS(cur):
    global cnt
    ch[cur]=1
    for i in range(n):
        if ch[i]==0 and g[cur][i]==1: #만약 아직 방문하지 않았고 연결되어 있다면
            ch[i]=1 #방문을 하고
            cnt+=1
            DFS(i) #탐색한다

if __name__=="__main__":
    n = int(input())
    k = int(input())
    g = [[0]*n for _ in range(n)]
    ch = [0]*(n+1)
    for i in range(k):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1 #양방향인 것을 고려한다
        g[b-1][a-1] = 1
    ch[0]=1
    cnt = 0
    DFS(0)
    print(cnt)


