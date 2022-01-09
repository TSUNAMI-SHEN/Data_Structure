//股票的最大利润，解释见notability
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, cost = INT_MAX;
        int n = prices.size();
        for (int i = 0; i < n; i++)
        {
            cost = min(cost, prices[i]);
            profit = max(profit, prices[i] - cost);
        }
        return profit;
    }
};
