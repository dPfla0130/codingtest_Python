import sys
sys.stdin=open("in1.txt", "r")

def DFS(L, W, t):
    global m
    #가지치기 1
    #앞으로 진행할 값 (모든 나머지 값들이 부분집합이 되었다고 생각했을 때)과 지금까지 값을 더했을 때
    #최대값보다 작으면 가지치기 한다
    if W+(total-t)<m:
        return
    #가지치기 2
    #현재 값이 제한 값보다 커질 때 가지치기 한다
    if W>c:
        return
    if L==n:
        if W>m:
            m = W
    else:
        DFS(L + 1, W + li[L], t+li[L])
        DFS(L + 1, W, t+li[L])

if __name__=="__main__":
    a = list(map(int, input().split()))
    c = a[0]
    n = a[1]
    li = [0]*n
    m = 0

    for i in range(n):
        li[i] = int(input())
    total = sum(li)
    DFS(0, 0, 0)
    print(m)
