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

def subsetSums3(nums, k):
    curr_nums = []
    curr_sum = [0]
    def dfs(i):
        if i == len(nums):
            if curr_sum[0] == k:
                print(curr_nums)
            return
        curr_nums.append(nums[i])
        curr_sum[0] += nums[i]
        dfs(i+1)
        curr_nums.pop()
        curr_sum[0] -= nums[i]
        dfs(i+1)
    dfs(0)

import time
def estimate_time(nums, k):
    nums1 = [1,2,3,4,5,6,7,8,9,10]
    k1 = 55
    start_time = time.time()
    subsetSum2(nums1,k1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    mn = len(nums) / 10 
    if mn < 1:
        mn = 1
    mk = k / 55
    if mk < 1:
        mk = 1
    estimate = elapsed_time * mn * mk 
    print(f"estimate: {estimate:.6f} seconds")

import random
# generate n numbers between -k, k
def generate_test_data(n,k):
    nums = [random.randint(-k,k) for i in range(n)]
    return [nums, k] 
    
nums = [-1,3,5,-2,8]
k = 7

subsetSums3(nums,k)
# a = subsetSum2(nums, k)
# print(a)
nums, k = generate_test_data(100, 100000)
estimate_time(nums, k)

start_time = time.time()
print(subsetSum2(nums,k))
stop_time = time.time()
print(f"Time taken: {stop_time-start_time:.6f} seconds")
