class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # 이미 정렬(비회전)된 경우 빠른 반환
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            # mid가 오른쪽 정렬 구간의 왼쪽 끝보다 크면,
            # 회전 지점(최소)은 오른쪽에 있다.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 최소값이 mid를 포함한 왼쪽 구간에 있다.
                right = mid
        return nums[left]
