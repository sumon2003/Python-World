#include<bits/stdc++.h>
using namespace std;

int dp[10][10];

int knapsack_01(int n, int w, int profit[], int wt[]) {
    if (n == 0 || w == 0) return 0;
    if (dp[n][w] != -1) return dp[n][w];

    if (wt[n - 1] > w) 
        return dp[n][w] = knapsack_01(n - 1, w, profit, wt);
    else
        return dp[n][w] = max(knapsack_01(n - 1, w, profit, wt),
                              profit[n - 1] + knapsack_01(n - 1, w - wt[n - 1], profit, wt));
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, w;
        cin >> n >> w;

        int profit[n], wt[n];
        for (int i = 0; i < n; i++) {
            cin >> profit[i];
        }

        for (int i = 0; i < n; i++) {
            cin >> wt[i];
        }

        memset(dp, -1, sizeof(dp));
        cout << knapsack_01(n, w, profit, wt) << endl;
    }

    return 0;
}
