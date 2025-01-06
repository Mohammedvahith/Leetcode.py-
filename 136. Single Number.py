def singleNumber(nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR each number with the current result
        return result

nums = [5, 2, 3, 1, 5, 2, 3, 4]
print(singleNumber(nums))
