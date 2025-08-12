class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []
        n = len(nums)

        for i in range(n - 2):
            # i 중복 스킵
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 조기 종료: 현재 수가 양수면 뒤도 모두 양수 → 합이 0 불가
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # left/right 중복 스킵
                    left_val, right_val = nums[left], nums[right]
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1

        return res
