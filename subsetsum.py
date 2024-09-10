# condition a: if nums == {} (empty set), False for all k
# condition b: if n == k, (where n is ith number of nums), True
# condition c: if row-1 == True (subset already True), True
# condition d: if k-n == True (in prev rows/ subset), True

# return table
def subset_sum_table(nums, k):
    min_val = min(nums)
    # for all positive integers

    if min_val > 0:
        min_val = 0

    num_cols = abs(min_val)+k+1
    # for negative need to extend table right
    if min_val < 0:
        num_cols += abs(min_val)

    dp = [[False]*num_cols for i in range(len(nums)+1)]

    for row in range(1, len(nums)+1):
        for col in range(num_cols):
            # check condition b,c,d
            current_sum = col + min_val
            b = nums[row-1] == current_sum

            c = dp[row-1][col]

            new_col = col - nums[row-1]
            is_valid_index = 0 <= col - nums[row-1] < num_cols
            d = is_valid_index and dp[row-1][new_col]

            dp[row][col] = b or c or d

    return dp

# returns solution set (assumes 1 solution)
def subset_sum(table, nums, k):
    res = []
    min_val = min(nums)
    if min_val > 0:
        min_val = 0
    row = len(table)-1
    col = len(table[0])-1+min_val # adjustment for start at sum k

    # case 1: no subset
    if not table[row][col]:
        return []

    # case 2: k in nums 
    for n in nums:
        if n == k:
            return [n]

    while row > 0 and col >= 0:
        # condition b 
        if nums[row-1] == col + min_val:
            res.append(nums[row-1])
            break
    
        # condition c
        elif table[row-1][col]:
            row -= 1

        # condition d 
        elif table[row-1][col-nums[row-1]]:
            res.append(nums[row-1])
            col -= nums[row-1]
            row -= 1

    return res

import time
def estimate_time(nums, k):
    nums1 = [1,2,3,4,5,6,7,8,9,10]
    k1 = 55
    start_time = time.time()
    subset_sum_table(nums1,k1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    mn = len(nums) / 10 
    if mn < 1:
        mn = 1
    mk = k / 55
    if mk < 1:
        mk = 1
    estimate = elapsed_time * mn * mk 
    print(f"Estimate time: {estimate:.6f} seconds")

import random
# generate n numbers between -k, k
def generate_test_data(n,k):
    nums = [random.randint(-k,k) for i in range(n)]
    return [nums, k] 
    
def get_test_data(filename):
    nums = []
    with open(filename, "r") as f:
        for line in f:
            d = float(line)
            d *= 100
            d = round(d)
            nums.append(int(d))
    return nums

# nums = [-1,-3,5,2,8]
# k = 7

# nums = [18, 52, 72, 92, 76, -83, 19, 74, -25, 69]
# nums = [-95, 34, -90, -99, -57, 27, 25, 94, -1, 56 ]
# k = 100
# nums = [2,3,-1]
# k = 4
nums = get_test_data("a.txt")
print(f"sun: {sum(nums)}")
k = 192354
# nums = [1, -2, 3, -1, 2, -3]
# k = 0
# a = subsetSum2(nums, k)
# print(a)
# nums, k = generate_test_data(1000, 100000)
estimate_time(nums, k)

start_time = time.time()
table = subset_sum_table(nums,k)
stop_time = time.time()
print(f"Time taken: {stop_time-start_time:.6f} seconds")

start_time = time.time()
a = subset_sum(table, nums, k)
print(k, a)
stop_time = time.time()
print(f"Time taken: {stop_time-start_time:.6f} seconds")