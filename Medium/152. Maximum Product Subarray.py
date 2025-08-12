class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 초기화
        curr_max = curr_min = ans = nums[0]

        for x in nums[1:]:
            # 음수면 부호 뒤집힘 효과 때문에 최대/최소 교환
            if x < 0:
                curr_max, curr_min = curr_min, curr_max

            # 현재 원소 하나로 새로 시작 vs 연장
            curr_max = max(x, curr_max * x)
            curr_min = min(x, curr_min * x)

            # 전역 최대 갱신
            ans = max(ans, curr_max)

        return ans
