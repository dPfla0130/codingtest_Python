def rotateImage(a):
    result = []
    for i in range(len(a)):
        sub = []
        for j in range(len(a)-1, -1 , -1):
            sub.append(a[j][i])
        result.append(sub)
    return result



if __name__ == "__main__":
    print(rotateImage([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))