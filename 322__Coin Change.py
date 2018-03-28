class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        pp = [0]
        print(pp)
        i = 1
        while i <= amount:
            t = len(coins) - 1
            minm = float("inf")
            while t >= 0:
                if i - coins[t] >= 0 and i - coins[t] < len(pp):
                    if pp[i - coins[t]] != -1:
                        minm = min(pp[i - coins[t]] + 1, minm)
                    else:
                        minm = minm
                t = t - 1
            if minm == float("inf"):
                pp.append(-1)
            else:
                pp.append(minm)
            # print (pp)
            i = i + 1
        if pp[-1] == float('inf'):
            return (-1)
        else:
            return pp[-1]

class Solution2(object):
    def coinChange2(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return dp[-1] if dp[-1]!=MAX else -1