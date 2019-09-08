#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main(){
    int n;
    cin >> n;
    int pp[n];
    int qq[n];
    for(int i=0;i<n;i++){
        scanf("%d",&pp[i]);
    }
    for(int i=0;i<n;i++){
        scanf("%d",&qq[i]);
    }
    int max_pp = 0;
    int result=0;
    int id, max_qq,len;
    int flag[n]={0};
    for(int i=0;i<n;i++){
        id = 0;
        max_qq = 0;
        len = 0;
        for(int j=0;j<n;j++){
            if(flag[j]==0 && max_qq<(qq[j]+2*max(0,pp[j]-max_pp))){
                id =j;
                max_qq = qq[j];
                max_qq = max_qq + 2*max(0,pp[j]-max_pp)
                len = pp[j];
            }
        }
        result = result + max_qq;
        flag[id] =1;
        max_pp = max(max_pp,len);
        cout<<result<<endl;
    }
    return 0;
}