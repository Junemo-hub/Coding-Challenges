from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # 계속 왼쪽 찾기
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        def findLast():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1  # 계속 오른쪽 찾기
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        return [findFirst(), findLast()]
