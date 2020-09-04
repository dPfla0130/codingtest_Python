import sys

sys.stdin=open("in.txt", "r")

num = int(input())

arr = [0]*(num)
result = [0]*(num)

for i in range(num):
    arr[i]= int(input())
result[0] = arr[0]
#연속으로 밟았을 때 1, 아닐 때 0
flg = 0
print(arr)
i=1
while True:

    print(i, result)
    if i==num-1 or i==num-2:

        result[-1] = result[i-1]+arr[-1]
        break
    if flg ==0:
        #연속으로 밟지 않았으므로, 다음것도 밟을 수 있다
        #다다음 계단 밟은 상황

        if arr[i] < arr[i+1]:
            result[i] = result[i-1]+arr[i+1]
            result[i+1]= result[i]
            i +=2
        else:
            result[i] = result[i-1]+arr[i]
            #연속으로 밟음
            flg=1
            i+=1
    else:
        result[i] = result[i-1]+arr[i+1]
        result[i + 1] = result[i]
        flg=0
        i+=2


print(result[-1])