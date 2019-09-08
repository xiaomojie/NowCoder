// 本题为考试多行输入输出规范示例，无需提交，不计分。
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main(){
    //freopen("1.in","r",stdin);
    int N;
    cin >> N;
    int dis[N];
    int wei[N];
    for(int i=0;i<N;i++){
        scanf("%d",&dis[i]);
    }
    for(int i=0;i<N;i++){
        scanf("%d",&wei[i]);
    }
    int maxdis = 0;
    int res=0;
    int maxid,maxwei,len;
    int mark[N]={0};
    for(int i=0;i<N;i++){
        maxid = 0;
        maxwei = 0;
        len = 0;
        for(int j=0;j<N;j++){
            if(mark[j]==0&&maxwei<(wei[j]+2*max(0,dis[j]-maxdis))){
                maxid =j;
                maxwei = (wei[j]+2*max(0,dis[j]-maxdis));
                len = dis[j];
            }
        }
        res = res + maxwei;
        mark[maxid] =1;
        maxdis = max(maxdis,len);
        cout<<res<<endl;
    }
    return 0;
}