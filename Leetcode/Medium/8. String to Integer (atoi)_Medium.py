
class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. 공백 무시
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        # 2. 빈 문자열 또는 전부 공백이면 0 반환
        if i >= n:
            return 0
        
        # 3. 부호 처리
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 4. 숫자 파싱
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # 5. overflow 체크: 곱하기 전에 체크
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                # 범위 넘으면 클램핑
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
        