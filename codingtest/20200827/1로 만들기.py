num = int(input())
result = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
i = 11

while i<=num:
    arr = []
    if i%3==0:
        arr.append(result[int(i/3)]+1)
    if i%2==0:
        arr.append(result[int(i/2)]+1)
    arr.append(result[i-1]+1)
    i+=1
    result.append(min(arr))

print(result[num])
