class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for index in range(n + 1):
            count.append(bin(index).count("1"))
        return count
