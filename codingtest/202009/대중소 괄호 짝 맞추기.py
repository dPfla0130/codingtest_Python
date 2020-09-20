def solution(s):
    answer = True
    stack = []

    for i in s:
        try:
            if i == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
            elif i == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif i == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            else:
                stack.append(i)
        except:
            return False
    if len(stack)>0:
        answer = False

    return answer

if __name__ == "__main__":
    print(solution(s="(){"))
