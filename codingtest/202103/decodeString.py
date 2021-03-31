def decodeString(s):
    stack = []
    StringResult = ''
    for i in s:
        if i == ']' and stack:
            string = ''
            while stack:
                string = stack.pop() + string
                if stack[-1] == '[':
                    stack.pop()
                    num = ''
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    string = string * int(num)
                    if stack:
                        if stack[-1] != '[':
                            stack[-1] = stack[-1] + string
                        else:
                            stack.append(string)
                    else:
                        stack.append(string)
                    break

        else:
            stack.append(i)
    result = ''
    if stack:
        result = StringResult.join(stack)
    return result

if __name__ == "__main__":
    print(decodeString("2[2[b]]"))
