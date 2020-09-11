def solution(v):
    answer = []
    x = []
    y = []
    for i in v:
        if i[0] not in x:
            x.append(i[0])
        else:
            x.remove(i[0])
        if i[1] not in y:
            y.append(i[1])
        else:
            y.remove(i[1])
    answer = x + y
    return answer

if __name__ == "__main__":
    print(solution(v=[[0, 0], [2, 2], [0, 2]]))

