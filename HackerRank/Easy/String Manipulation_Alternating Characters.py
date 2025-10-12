def alternatingCharacters(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count



# 생각을 통해 혼자서 풀음
# for 뒤에 문법만 좀 헷갈림.