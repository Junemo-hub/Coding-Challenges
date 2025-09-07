class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = 0
        xor_nums = 0

        # XOR from 0 to n
        for i in range(n + 1):
            xor_all ^= i

        # XOR of all numbers in the array
        for num in nums:
            xor_nums ^= num

        # The missing number is the XOR of the two results
        return xor_all ^ xor_nums
