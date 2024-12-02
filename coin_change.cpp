#include<bits/stdc++.h>
using namespace std;

#define mx 1000
int dp[mx][mx];

int counts(int coins[], int n, int target_amount)
{
	if (target_amount == 0) 
		dp[n][target_amount] = 1;
	if (target_amount < 0 || n == 0) 
		dp[n][target_amount] = 0;

	if(dp[n][target_amount] == -1)
		dp[n][target_amount] = counts(coins, n, target_amount - coins[n-1]) + 
		                       counts(coins, n - 1, target_amount);

	return dp[n][target_amount];
}

int main()
{
	int n, target_amount;
	
	cout << "Enter the number of coin types: ";
	cin >> n;

	int coins[n];
	
	cout << "Enter the coin denominations: ";
	for(int i = 0; i < n; i++)
		cin >> coins[i];

	cout << "Enter the target amount: ";
	cin >> target_amount;

	memset(dp, -1, sizeof(dp));

	cout << "Number of ways to make " << target_amount << " is: " << counts(coins, n, target_amount) << endl;

	return 0;
}
