class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])  # 복사해서 저장 (중요)
                return

            for number in nums:
                if number in path:
                    continue  # 이미 고른 건 생략
                backtrack(path + [number])  # 새로 선택된 숫자 추가

        backtrack([])
        return result