def DFS(start, finish, signs):
    visit = []
    stack = []
    stack.append(start)

    while stack:
        now = stack.pop()
        for i in range(len(signs)):
            if signs[now][i] == 1 and i not in visit:
                if i == finish:
                    return 1
                stack.append(i)
                visit.append(i)
    return 0


def solution(n,signs):
    answer = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(DFS(i, j, signs))
        answer.append(tmp)

    return answer

if __name__ == "__main__":
    print(solution(n=3, signs=[[0,0,1],[0,0,1],[0,1,0]]))
