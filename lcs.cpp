#include<bits/stdc++.h>
using namespace std;

int lcs(string &S1, string &S2, int m, int n){
    if (m == 0 || n == 0)
        return 0;
    if (S1[m - 1] == S2[n - 1])
        return 1 + lcs(S1, S2, m - 1, n - 1);
    else {
        return max(lcs(S1, S2, m, n - 1), 
        	lcs(S1, S2, m - 1, n));
    }
}

int main() {
    string S1, S2;
    cin >> S1;
    cin >> S2;
    int m = S1.size();
    int n = S2.size();
    cout << lcs(S1, S2, m, n) << endl;//Length of the lcs
    return 0;
}
