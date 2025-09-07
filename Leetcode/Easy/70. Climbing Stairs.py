class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# 위 솔루션은 시간 초과
    
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(k):
            if k in memo:
                return memo[k]
            if k == 1:
                return 1
            if k == 2:
                return 2
            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]

        return dfs(n)

# 보편적인 효율적인 방법

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# 제일 효율적인 방법
