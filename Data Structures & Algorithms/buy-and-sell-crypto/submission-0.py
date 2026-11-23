class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        stockList = [101, 0, 0]
        for item in prices:
            if stockList[1] < item:
                stockList[1] = item
            if stockList[0] > item:
                stockList[0] = item
                stockList[1] = 0
            if stockList[2] < stockList[1] - stockList[0]:
                stockList[2] = stockList[1] - stockList[0]

        return stockList[2]
            