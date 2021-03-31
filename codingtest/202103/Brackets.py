# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    for i in S:
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 0
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0
        else:
            stack.append(i)

    if stack:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(solution("{[()()]}"))