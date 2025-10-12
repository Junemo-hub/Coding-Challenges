#1번 풀이
from collections import Counter  # MUST be here, at the top-level

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    mag_counts = Counter(magazine)
    note_counts = Counter(note)

    for word in note_counts:
        if mag_counts[word] < note_counts[word]:
            print("No")
            return
    print("Yes")


# 2번 풀이
def checkMagazine(magazine, note):
    mag_counts = {}

    # 단어 개수 세기
    for word in magazine:
        mag_counts[word] = mag_counts.get(word, 0) + 1

    # 노트 단어가 magazine에 충분히 있는지 확인
    for word in note:
        if mag_counts.get(word, 0) == 0:
            print("No")
            return
        mag_counts[word] -= 1

    print("Yes")



# word를 가져오는게 get으로 할 수 있다는걸 생각 중임.
