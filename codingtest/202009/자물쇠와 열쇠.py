import copy
def rotate_90(m, i, cnt):
    if cnt == i:
        return m
    else:
        N = len(m)
        ret = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
        m = rotate_90(ret, i, cnt+1)

    return m

def chk(key, lock):
    tmp = copy.deepcopy(lock)
    for i in range(len(key)):
        for j in range(len(key)):
            


def solution(key, lock):
    answer = True
    n = 3
    m = 3
    for i in range(n):
        lock[i] = [0]*(m - 1) + lock[i] + [0]*(m - 1)
    for i in range(m-1):
        lock.insert(i, [0]*(2*m + n -2))
    for i in range(m-1):
        lock.append([0]*(2*m + n -2))

    for i in range(1, 4):
        #0, 90, 180, 270도 회전하면서 확인한다
        key = rotate_90(key, i, 0)

    for i in range(len(lock)):
        print(lock[i])
    print()

    chk(key, lock)
    return answer

if __name__ == "__main__":
    print(solution(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
