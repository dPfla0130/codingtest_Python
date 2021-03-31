# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort(reverse=True)
    print(A)
    return max(A[0] * A[1] * A[2], A[0] * A[-1] * A[-2])


if __name__ == "__main__":
    print(solution([3, -1, 2, -3]))