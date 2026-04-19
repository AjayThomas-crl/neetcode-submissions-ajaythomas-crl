class Solution {
    public boolean findSubsetSum(int[][] dp, int[] arr,int i,int target){
        if(target==0)return true;
        if(i==0)return (arr[i]==target);
        if(dp[i][target]!=-1){
            if(dp[i][target]==1)return true;
            else return false;
        }
        if(arr[i]<target){
            dp[i][target]=findSubsetSum(dp,arr,i-1,target-arr[i])?1:0;
        }else{
            dp[i][target]=findSubsetSum(dp,arr,i-1,target)?1:0;
        }
        if(dp[i][target]==1)return true;
            else return false;
    }
    public boolean canPartition(int[] nums) {
        int sum=0;
        for(int n:nums)sum+=n;
        if(sum%2==0){
            int[][] dp=new int[nums.length][(sum/2)+1];
            for(int [] row:dp){
                 Arrays.fill(row,-1);
            }
           
            return findSubsetSum(dp,nums,nums.length-1,sum/2);
        }

     
        else
            return false;
    }
}
