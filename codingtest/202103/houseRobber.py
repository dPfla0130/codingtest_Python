def houseRobber(nums):
    dp = [0]*len(nums)
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)
    else:
        for i in range(len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            print(dp)
    return dp[-1]



if __name__ == "__main__":
    print(houseRobber([1, 1, 1]))

