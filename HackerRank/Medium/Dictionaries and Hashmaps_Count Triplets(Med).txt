from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    potential = defaultdict(int)
    pairs = defaultdict(int)
    count = 0

    for val in arr:
        if val in pairs:
            count += pairs[val]

        if val in potential:
            pairs[val * r] += potential[val]

        potential[val * r] += 1

    return count    

# 처음에 생각했던 arr에서 r, r^2 곱한걸 다 찾는다는건 N^3으로 매우 시간 소모가 큼
# 하나씩 지나가면서 넣는 이 해쉬맵 방식이 너무 헷갈리지만 효용이 매우 높은듯
# 이걸 항상 숙지해 두자.