# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    arr = []
    s = 0
    sumA = sum(A)
    answer = []
    if len(A)==2:
        arr.append(A[0])
    else:
        for i in range(len(A)):
            s += A[i]
            arr.append(s)
    for i in range(len(arr)):
        answer.append(abs(sumA - arr[i]*2))
    return min(answer)


if __name__ == "__main__":
    print(solution([-1, -10, 1]))