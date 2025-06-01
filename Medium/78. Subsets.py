class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, path):
            res.append(path[:])  # 현재 부분집합 추가

            for i in range(start, len(nums)):
                path.append(nums[i])     # 원소 추가
                dfs(i + 1, path)         # 다음 단계 재귀
                path.pop()               # 원소 제거 (백트래킹)

        dfs(0, [])
        return res