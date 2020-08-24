import sys
sys.stdin=open("in1.txt", "r")

#조합 구하기
def DFS(L, s):
    global cnt
    if len(p)==k:
        if sum(p)%m==0:
            cnt+=1
        return
    else:
        #반복문 위치 중요
        for i in range(s, n):
            if ch[i]==0:
                ch[i]=1
                p.append(arr[i])
                DFS(L+1, i+1)
                ch[i]=0
                p.pop()

if __name__=="__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    p = []
    ch = [0]*(n+1)
    m = int(input())
    cnt =0
    DFS(0, 0)
    print(cnt)