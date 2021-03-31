def firstDuplicate(a):
    #시간복잡도 Best O(1), Worst O(n)
    dup = set()

    for i in a:
        if dup and i in dup:
            return i
        dup.add(i)

    return -1

if __name__ == "__main__":
    print(firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8]))