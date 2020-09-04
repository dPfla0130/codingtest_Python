import sys

n = 1
q = [0]*n
si = [[0, 3], [2, 5], [4, 2], [5, 3]]
ct = 0
wt = 0
j = 0
while True:

    if j==len(si):
        break
    # 만약 상담시간이 끝나면 창구 비어준다
    if ct in q:
        q[q.index(ct)]=0
    # 만약 빈창구가 있다면
    if 0 in q:
        if ct>= si[j][0]:
            i = q.index(0)
            q[i] = ct + si[j][1]
            j+=1

    for p in range(j, len(si)):
        if ct>=si[p][0]:
            wt+=1


    ct+=1
print(wt)