def kthLargestElement(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

if __name__ == "__main__":
    print(kthLargestElement([7, 6, 5, 4, 3, 2, 1], 2))