# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    str2 = ""
    arr = 0
    stack = []
    answer = []

    while N > 0:
        str2 += str(N%2)
        N = N//2
    str2 = str2[::-1]

    for i in str2:
        if i=='1':
            if len(stack)>0:
                stack.pop(0)
                if arr!=0:
                    answer.append(arr)
                    arr = 0
            stack.append(i)
        else:
            arr+=1
    if len(answer)==0:
        return 0
    else:
        return max(answer)


if __name__ == "__main__":
    print(solution(32))
    # print(solution("6789", 1))
    # print(solution("1231234", 3))
    # print(solution("4177252841", 2))