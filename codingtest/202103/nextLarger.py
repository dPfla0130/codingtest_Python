def nextLarger(a):
    stack = []
    result = []
    stack.append((a[0], 0))
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                result.append(a[j])
                break
            if j == len(a)-1:
                result.append(-1)
    result.append(-1)
    return result



if __name__ == "__main__":
    print(nextLarger([10, 3, 12, 4, 2, 9, 13, 0, 8, 11, 1, 7, 5, 6]))
