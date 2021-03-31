# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    stack = []
    for i in range(len(A)):
        if i == 0:
            stack.append([A[i], B[i]])
        else:
            if stack[-1][1] == 1 and B[i] == 0:
                if stack[-1][0] < A[i]:
                    while True:
                        stack.pop()
                        if len(stack) == 0:
                            stack.append([A[i], B[i]])
                            break
                        if stack[-1][1] == B[i]:
                            stack.append([A[i], B[i]])
                            break
                        if stack[-1][0] > A[i]:
                            break
            else:
                stack.append([A[i], B[i]])

    return len(stack)

if __name__ == "__main__":
    print(solution([4, 3, 2, 6, 5], [1, 1, 1, 0, 1]))