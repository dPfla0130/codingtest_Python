import sys
sys.stdin=open("in1.txt", "r")

#순열조합 구하기
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L] = i
                #정해진 수열과 이항계수의 곱한 값을 더한다
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__=="__main__":
    n, f = map(int, input().split())
    p = [0]*n #순열만들기
    b = [1]*n #이항계수 저장하기
    ch = [0]*(n+1)
    for i in range(1, n): #이항계수 구하기 ((n-1)C1, (n-1)C2....)
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)
