def solution(n):
    answer = []
    li = []
    s = 0
    for i in range(1, n+1):
        s+=i
    num = 1
    for i in range(1, n+1):
        tmp = [0]*i
        li.append(tmp)

    while num <= s:
        for i in range(n):
            li[i][0] = num
        num += 1
    return answer

if __name__ == "__main__":
    print(solution(n = 4))

