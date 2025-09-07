class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # 지금까지의 최소값
        max_profit = 0            # 최대 수익

        for price in prices:
            if price < min_price:
                min_price = price  # 최소값 갱신
            else:
                max_profit = max(max_profit, price - min_price)  # 수익 갱신

        return max_profit
