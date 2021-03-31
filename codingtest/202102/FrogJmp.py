# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(X, Y, D):
    # write your code in Python 3.6
    dis = Y-X
    if dis == 0:
        return 0
    if dis%D ==0:
        return dis//D
    else:
        return dis//D+1

if __name__ == "__main__":
    print(solution(1, 1000, 10))