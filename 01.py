def knapsack(cap, *items):
    dp = [[0] * (cap + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for w in range(cap + 1):
            if items[i - 1][0] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][0]] + items[i - 1][1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[-1][-1]