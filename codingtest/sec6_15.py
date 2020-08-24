import sys
sys.stdin=open("in2.txt", "r")

#경로탐색
def DFS(L):
    global cnt
    #만약에 최종 노드에 도달한다면
    if L==n-1:
        #가지 수를 카운트한다
        cnt+=1
        return
    else:
        for i in range(n):
            #노드가 연결되어 있고 방문 전이라면
            if ch[i]==0 and g[L][i]==1:
                #노드를 방문한다
                ch[L] = 1
                DFS(i)
                #방문한 노드를 체크해제한다(방문하지 않게 됨)
                ch[i]=0

if __name__=="__main__":
    n, m = map(int, input().split())
    g = [[0]*(n) for _ in range(n)]
    ch = [0]*(n)
    cnt = 0
    #그래프 만들기
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1

    ch[0] = 1
    DFS(0)
    print(cnt)