

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        m_area = 0
        
        while left < right:
            curr = min(height[left], height[right]) * (right - left)
            m_area = max(m_area, curr)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return m_area








# time exceeded solution #
class Solution:
    def maxArea(self, height: List[int]) -> int:
        m_area = 0
        n = len(height)
        
        for i in range(n):
            for j in range(i+1, n):
                curr = min(height[i], height[j]) * (j - i)
                m_area = max(m_area, curr)
        
        return m_area
