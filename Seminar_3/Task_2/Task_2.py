nums = [2, 3, 4, 5, 6]

def nums_pair_product(nums):
    prod = []
    half_len = len(nums) // 2
    for i in range(0, half_len):
        prod.append(nums[i] * nums[-i -1])
    if len(nums) % 2 != 0:
        prod.append(nums[half_len] ** 2)
    return prod

print(nums_pair_product(nums))
print(nums_pair_product(nums=[2, 3, 5, 6]))