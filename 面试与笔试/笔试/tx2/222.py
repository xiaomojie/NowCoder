#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int t,k;
    cin >> t >> k;
    vector<int> left(t,0);
    vector<int> right(t,0);

    int len = 0;
    int m = 0;
    for(int i = 0; i < t; i++){
        cin >> left[i];
        cin >> right[i];
        len = max(len, right[i]);
    }
    int index = 0;
    int n = len+1;
    vector<int> dp(n,0);

    for(int i=0;i<=len;i++){
        if(i >= k){
            dp[i]=dp[i-1]+dp[i-k];
        }else{
            dp[i]=1;
        }
    }
    for(int i = 0; i < t; i++){
        int res = 0;
        for(int j = left[i];j <= right[i];j++ ){
            res += dp[j];
        }
        cout << res % (1000000000+7) << endl;
    }
    return 0;
}