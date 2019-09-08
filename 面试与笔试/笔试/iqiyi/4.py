class Solution {
public:
    int f(string S) {
        int N = S.length() + 1;
        int MOD = 1e9 + 7;
        int dp[202][202] = {};
        dp[1][1] = 1;
        for (int i = 2; i <= N; ++i) {
            // length is i
            for (int j = 1; j <= i; ++j) {
                // end with j
                if (S[i - 2] == 1) {
                    dp[i][j] = (dp[i][j-1] + (dp[i-1][i-1] - dp[i-1][j-1]) % MOD) % MOD;
                } else {
                    dp[i][j] = (dp[i][j-1] + (dp[i-1][j-1] - dp[i-1][0]) % MOD) % MOD;
                }
            }
        }
        return (dp[N][N] + MOD) % MOD;
    }
};