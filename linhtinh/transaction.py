class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = []
        dp.append(0)
        dp.append(1)
        
        for i in range(2,n+1):
            dp.append(dp[i-1]+i)
            if dp[i] > n:
                return i-1
a = Solution
b =a.arrangeCoins(a,12)
print(b)