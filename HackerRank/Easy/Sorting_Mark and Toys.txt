def maximumToys(prices, k):
    prices.sort()  
    count = 0
    total = 0

    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break

    return count
   

# 낮은거 부터 더하는 데 쉬운 생각이지만 좋음
# sort 함수 활용~!
