class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(f"left: {left}, mid: {mid}, right: {right}, nums[mid]: {nums[mid]}")  # 디버깅용 출력

            if nums[mid] == target:
                return mid

            # 왼쪽 반이 정렬된 경우
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 오른쪽 반이 정렬된 경우
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1