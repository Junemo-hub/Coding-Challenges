class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = best = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)  # x에서 새로 시작 vs 이어붙이기
            best = max(best, curr)
        return best
