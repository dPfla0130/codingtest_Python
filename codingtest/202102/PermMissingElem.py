# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A)==0:
        return 1
    A.sort()
    print(A)
    s = 0
    i = 0
    while i <= A[-1]:
        s += i
        i += 1
    if s - sum(A) == 0:
        if A[0] != 1:
            return 1
        else:
            return A[-1] + 1
    else:
        return s - sum(A)


if __name__ == "__main__":
    print(solution([3]))