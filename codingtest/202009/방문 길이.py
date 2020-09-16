def solution(dirs):
    cur = [0, 0]
    stack = []
    #스택에 현재 위치와 다음 위치를 계산하여 담는다
    for i in dirs:
        if i == "U":
            next = [cur[0], cur[1] + 1]
        elif i == "D":
            next = [cur[0], cur[1] - 1]
        elif i == "R":
            next = [cur[0] + 1, cur[1]]
        else:
            next = [cur[0] - 1, cur[1]]
        #만약 범위에 맞지 않으면 명령어 무시
        if -5 <= next[0] <= 5 and -5 <= next[1] <= 5:
            #만약 갔던 길이라면 스택에 포함하지 않는다
            if [cur, next] not in stack and [next, cur] not in stack:
                stack.append([cur, next])
            cur = next

    answer = len(stack)

    return answer

if __name__ == "__main__":
    print(solution(dirs="ULRRL"))

