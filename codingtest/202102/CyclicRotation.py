# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if len(A)==0:
        return []
    else:
        K = K%len(A)

    answer = [0]*len(A)
    for i in range(len(A)):
        if i+K < len(A):
            answer[i+K] = A[i]
        else:
            answer[0:K] = A[i:]
            break

    return answer



if __name__ == "__main__":
    print(solution([1, 1, 2, 3, 5], 42))