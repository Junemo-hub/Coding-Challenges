class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 파이썬은 정수 크기 제한이 없어서, 32비트 마스크를 직접 씀
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # 1) 합 계산 (올림수 제외)
            _sum = (a ^ b) & MASK
            # 2) 올림수 계산
            carry = ((a & b) << 1) & MASK
            # 다음 라운드
            a, b = _sum, carry

        # 음수 처리
        return a if a <= MAX_INT else ~(a ^ MASK)
