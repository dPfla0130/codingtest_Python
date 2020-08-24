import sys
#sys.stdin=open("in1.txt", "r")

def DFS(L, sum):
    #시간 복잡도 줄이기(합의 절반을 넘어가면 안된다)
    if sum>total//2:
        return
    if L==n:
        if sum==(total-sum): #만약 부분집합의 합이 전체집합의 합에서 뺀 것과 같다면
            print("YES") #같다
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])#부분집합에 포함시킬 때 
        DFS(L+1, sum)#부분집합에 포함시키지 않을 때

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")