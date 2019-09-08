#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int t,k;
    cin >> t >> k;
    int len = 0;
    vector<int> start(t, 0);
    vector<int> end(t, 0);
    vector<int> dp(len+1, 0);
    for(int i = 0; i < t; i++){
        cin >> start[i];
        cin >> end[i];
        len = max(len, end[i]);
    }
    int m = 0;
    for(; m <= len; m++){
        if(m >= k){
            dp[m] = dp[m-1] + dp[m-k];
        }else{
            dp[m] = 1;
        }
    }

    for(int i = 0; i<t; i++){
        int out = 0;
        for(int j = start[i]; j <= end[i]; j++){
            out += dp[j];
        }
        cout << out  <<endl;

    }
    return 0;

}
