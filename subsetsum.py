
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

# condition a: if nums == {} (empty set), False for all k
# condition b: if n == k, (where n is ith number of nums), True
# condition c: if row-1 == True (subset already True), True
# condition d: if k-n == True (in prev rows/ subset), True

def subsetSum2(nums, k):
    min_val = min(nums)
    # for all positive integers
    if min_val > 0:
        min_val = 0
    num_cols = abs(min_val)+k+1
    dp = [[False]*num_cols for i in range(len(nums)+1)]

    for row in range(1, len(nums)+1):
        for col in range(num_cols):
            # check condition b,c,d
            current_sum = col - abs(min_val)
            b = nums[row-1] == current_sum

            c = dp[row-1][col]

            new_col = col - nums[row-1]
            is_valid_index = 0 <= col - nums[row-1] < num_cols
            d = is_valid_index and dp[row-1][new_col]

            dp[row][col] = b or c or d

    return dp[-1][-1]

nums = [-1,3,5,-2,8]
k = 7
a = subsetSum2(nums, k)

print(a)