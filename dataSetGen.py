import random as r

target = 1923.54
total = 0
nums = []

while total < target:
    v = round(r.random() * 400, 2)
    nums.append(v)
    total += v

nums.append(round(target - total, 2))

print(nums)
print(sum(nums))

with open("a.txt", "w") as f:
    for n in nums:
        f.write(f"{n}\n")