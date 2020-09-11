from collections import Counter
def solution(N, stages):
    answer = []
    c = Counter(stages)
    fault = [(0, 0)] * (N)
    l = len(stages)

    for i in range(1, N+1):
        if i==N+1:
            break
        l -= c[i-1]
        print(i, c[i], l)

        if l==0 and c[i]==0:
            fault[i-1] = (0, i)
        else:
            fault[i-1] = (c[i]/l, i)
    fault = sorted(fault, key= lambda x: (-x[0], x[1]))

    for i in fault:
        if i[1]==N+1:
            continue
        else:
            answer.append(i[1])
    return answer

if __name__ == "__main__":
    print(solution(N=4, stages= [4, 3, 2]	))

