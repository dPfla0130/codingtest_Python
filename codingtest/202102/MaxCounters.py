# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    answer = [0]* N

    for i in A:
        if i == N+1:
            answer = [max(answer)] * N
        else:
            answer[i-1] +=1
    return answer


if __name__ == "__main__":
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))