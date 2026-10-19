class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [amount + 1] * (amount + 1)
        DP[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    DP[i] = min(DP[i], 1 + DP[i - coin])
        return DP[amount] if DP[amount] != amount + 1 else -1
        