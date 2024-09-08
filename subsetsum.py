
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

# condition 1: if nums == {} (empty set), False for all k
# condition 2: if n == k, (where n is ith number of nums), True
# condition 3: if row-1 == True (subset already True), True
# condition 4: if k-n == True (in prev rows/ subset), True

def subsetSum2(nums, k):
    minVal = min(nums)
    dp = [[False]*(abs(minVal)+k+1) for i in range(len(nums)+1)]

    for row in range(1, len(nums)+1):
        for col in range(abs(minVal)+k+1):
            # check condition 2,3,4
            a = nums[row-1] == col - abs(minVal)
            b = dp[row-1][col]
            c =  0 <= col - nums[row-1] < abs(minVal)+k+1 and dp[row-1][col - nums[row-1]]

            dp[row][col] = a or b or c

    return dp[-1][-1]

nums = [-1,3,5,-2,8]
k = 7
a = subsetSum2(nums, k)

print(a)