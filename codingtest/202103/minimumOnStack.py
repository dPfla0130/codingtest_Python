def minimumOnStack(operations):
    stack = []
    result = []
    for operation in operations:
        operation = operation.split(" ")
        if operation[0] == "push":
            stack.append(int(operation[1]))
        elif operation[0] == "pop" and stack:
            stack.pop()
        elif operation[0] == "min" and stack:
            result.append(min(stack))
    return result



if __name__ == "__main__":
    print(minimumOnStack(["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]))
