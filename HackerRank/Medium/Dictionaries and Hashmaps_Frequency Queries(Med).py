from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = defaultdict(int)       
    freqCount = defaultdict(int)  
    res = []

    for op, val in queries:
        if op == 1:
            old = freq[val]
            freq[val] += 1
            freqCount[old] -= 1
            freqCount[old + 1] += 1

        elif op == 2:
            if freq[val] > 0:
                old = freq[val]
                freq[val] -= 1
                freqCount[old] -= 1
                freqCount[old - 1] += 1

        elif op == 3:
            res.append(1 if freqCount[val] > 0 else 0)

    return res

#    freq = defaultdict(int)       # 각 숫자의 등장 횟수 (숫자별 빈도)
#   freqCount = defaultdict(int)  # 특정 빈도를 가진 숫자의 개수
#  res = []                      # 결과 저장 리스트 (type 3 query)
# 등장횟수, 번호 자체를 2개를 세는 로직을 생각해서 2개를 조정하는 게 이 로직의 핵심인듯.
