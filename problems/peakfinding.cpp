#include <bits/stdc++.h>
#pragma warning(disable : 4996) // _CRT_SECURE_NO_WARNINGS

using namespace std;


int findPeakElement(int nums[], int len)
{
    int L = 0;
    int R = len-1;
    while(L < R){
        int m = (L+R+1) / 2;
        if (nums[m - 1] > nums[m])
            R = m-1;
        else
            L = m;
    return nums[L];
    }

};

int main(){
    int nums[] = {1,2,3,1};
    int len = sizeof(nums)/sizeof(nums[0]);    
    int r = findPeakElement(nums, len);
    cout << r <<endl;
    return 0;
}