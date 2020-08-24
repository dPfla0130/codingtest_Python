#Queue 사용
import sys
sys.stdin = open("in2.txt", "r")
arr = input()
num = int(input())

for i in range(num):
    q = []
    flag = 1
    for k in range(len(arr)):
        q.append(arr[k])

    cur = input()
    for j in cur:
        if len(q)>0 and j==q[0]:
            q.pop(0)
        if j in q[1:]:
            flag = 0
            continue
    if flag!=0 and len(q)==0:
        print("#"+str(i+1)+" YES")
    else:
        print("#"+str(i+1)+" NO")
