# #include <iostream>
# #include <cstdio>
# #include <vector>
# #include <algorithm>
#
# using namespace std;
#
# int main(){
#     int t,k;
#     cin >> t >> k;
#     int max_n = 0;
#     vector<int> minlen(t, 0);
#     vector<int> maxlen(t, 0);
#     for(int i = 0; i < t; i++){
#         cin >> minlen[i];
#         cin >> maxlen[i];
#         max_n = max(max_n, maxlen[i]);
#     }
#     vector<int> dp(max_n+1, 0);
#     for(int i = 0; i <= max_n; i++){
#         if(i<k){
#             dp[i] = 1;
#         }else{
#             dp[i] = dp[i-1] + dp[i-k];
#         }
#     }
#     for(int i = 0; i<t; i++){
#         int res = 0;
#         for(int j = minlen[i]; j <= maxlen[i]; j++){
#             res += dp[j];
#         }
#         cout << res<<endl;
#     }
#     return 0;
#
# }



