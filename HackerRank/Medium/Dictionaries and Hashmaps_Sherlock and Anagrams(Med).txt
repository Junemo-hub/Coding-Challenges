from collections import defaultdict


def sherlockAndAnagrams(s):
    substr_count = defaultdict(int)
    
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substr = s[start:end]
            key = ''.join(sorted(substr)) 
            substr_count[key] += 1

    result = 0
    for count in substr_count.values():
        if count > 1:
            result += (count * (count - 1)) // 2  

    return result


# collections랑 defaultdict를 써야했군. -> 이 개념 헷갈리지만 숙지 필요
# key = ''.join(sorted(substr)) 라는 걸로 key값을 넣는 것도 중요.