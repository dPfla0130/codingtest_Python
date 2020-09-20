answer = 0
def DFS(n, m, weights, w):
    global answer
    if n == len(weights) or w == m:
        if w == m:
            answer += 1

        return
    else:
        DFS(n + 1, m, weights, w + weights[n])
        DFS(n + 1, m, weights, w)

def solution(m, weights):
    DFS(0, m, weights, 0)
    return answer

if __name__ == "__main__":
    print(solution(m = 3000, weights=[500, 1500, 2500, 1000, 2000]))