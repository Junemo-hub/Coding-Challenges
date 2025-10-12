def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 2)  

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    max_value = 0
    current = 0

    for value in arr:
        current += value
        max_value = max(max_value, current)

    return max_value

# Hard 문제로 매우매우 어려움
# 차이값을 저장해두고 합계로 가야지만 계산 초과가 안걸림.
# a,b,k 등으로 활용하는게 너무 어렵네. (자동 unpack)