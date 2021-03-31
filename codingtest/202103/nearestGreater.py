def nearestGreater(a):
    near = []
    middle = len(a)//2
    if len(a) == 1:
        return [-1]
    for i in range(0, len(a)):
        if i < middle:
            for j in range(i+1, len(a)):
                if 2*i - j >= 0:
                    if a[i] < a[2*i - j]:
                        near.append(2*i - j)
                        break
                    if a[i] < a[j]:
                        near.append(j)
                        break
                else:
                    if a[i] < a[j]:
                        near.append(j)
                        break
                if j==len(a)-1:
                    near.append(-1)

        else:
            for j in range(i-1, -1, -1):
                if a[i] < a[j]:
                    near.append(j)
                    break
                if 2*i - j < len(a):
                    if a[i] < a[2*i - j]:
                        near.append(2*i - j)
                        break
                if j == 0:
                    near.append(-1)
    return near


if __name__ == "__main__":
    print(nearestGreater([66, 33, 18, 80, 95, 65, 69, 46, 10, 3]))