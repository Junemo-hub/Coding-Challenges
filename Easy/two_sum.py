class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # mapping system
        index_map = {}

        # finding needed value
        for i, num in enumerate(nums):
            # calculating needed value
            needed_value = target - num

            # found needed value in map
            if needed_value in index_map:
                return [index_map[needed_value], i]

            # map number storing
            index_map[num] = i


# ✅ 테스트 코드 (직접 실행해볼 수 있도록 추가)
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1] 출력