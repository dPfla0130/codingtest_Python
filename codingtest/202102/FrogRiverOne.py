def solution(X, A):
    # write your code in Python 3.6
    arr = [0] * X
    for i, idx in enumerate(A):
        if idx <= X:
            arr[idx-1] = 1
            if 0 not in arr:
                return i
    return -1

if __name__ == "__main__":
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))