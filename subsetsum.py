
def subsetSum(nums, k):
    dp = [[False]*(k+1) for i in range(len(nums)+1)]
    for row in range(1, len(nums)+1):
        for col in range(k+1):
            if nums[row-1] == col:
                dp[row][col] = True
            if dp[row-1][col]:
                dp[row][col] = True
            if col - nums[row-1] > 0 and dp[row-1][col - nums[row-1]]:
                dp[row][col] = True
    return dp

def subsetSum2(nums, k):
    minVal = min(nums)
    sums = [i for i in range(minVal, k+1)]
    dp = [[False]*(abs(minVal)+k+1) for i in range(len(nums)+1)]

    for row in range(1, len(nums)+1):
        for col in range(abs(minVal)+k+1):
            if nums[row-1] == sums[col]:
                dp[row][col] = True

            if dp[row-1][col]:
                dp[row][col] = True

            if nums[row-1] >= 0:
                if col - nums[row-1] >= 0 and dp[row-1][col - nums[row-1]]:
                    dp[row][col] = True
            else:
                if col - nums[row-1] < len(sums) and dp[row-1][col - nums[row-1]]:
                    dp[row][col] = True

    return dp

nums = [-1,3,5,-2,8]
k = 7
a = subsetSum2(nums, k)

print(a)