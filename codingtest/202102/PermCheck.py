# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    m = max(A)
    s = m*(m+1)//2
    if sum(A) != s:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(solution([4, 1, 3, 2]))