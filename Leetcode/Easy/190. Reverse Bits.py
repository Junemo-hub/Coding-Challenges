class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1           # result를 왼쪽으로 한 칸 이동
            result |= (n & 1)      # n의 마지막 비트를 result에 붙임
            n >>= 1                # n을 오른쪽으로 한 칸 이동
        return result


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = result << 1               # 왼쪽으로 비트 1칸 밀기
            last_bit = n & 1                   # n의 마지막 비트 뽑기
            result = result | last_bit         # result의 오른쪽에 그 비트 채우기
            n = n >> 1                         # n 오른쪽으로 1칸 shift
        return result
