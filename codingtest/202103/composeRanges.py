def composeRanges(nums):
    result = []
    i = 0
    while i < len(nums):
        chk = 0
        for j in range(i+1, len(nums)):
            if nums[j] != nums[j-1] + 1:
                chk = 1
                result.append([i, j-1])
                i = j
                break
        if chk == 0:
            i += 1

    res = []
    if result and result[-1][1] != len(nums)-1:
        result.append([result[-1][1]+1, len(nums)-1])
    if not result:
        result.append([0, len(nums)-1])
    for i in result:
        if i[0] == i[1]:
            res.append(str(nums[i[0]]))
        else:
            s = str(nums[i[0]]) + "->" + str(nums[i[1]])
            res.append(s)
    return res


if __name__ == "__main__":
    print(composeRanges([-1]))

