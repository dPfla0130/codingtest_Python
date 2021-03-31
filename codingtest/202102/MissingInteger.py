# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A = list(set(A))
    A.sort()
    cnt = 1
    print(A)
    for i in A:
        if i <= 0:
            continue
        if i != cnt:
            return cnt
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution([0, 299, 1]))