from collections import Counter


def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)

    deletions = 0
    all_chars = set(counter_a.keys()).union(counter_b.keys())

    for char in all_chars:
        deletions += abs(counter_a.get(char, 0) - counter_b.get(char, 0))

    return deletions


# collections, counter에 익숙해질 필요 있음.
# counter_이라는 표현에 익숙해 져야 할 듯.