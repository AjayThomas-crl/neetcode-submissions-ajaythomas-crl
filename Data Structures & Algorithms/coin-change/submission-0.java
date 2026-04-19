class Solution {
    int INF = (int)1e9;
    public int mincoin(int[][] dp,int[] arr,int i,int target){
        if(i==0){
            if(target%arr[0]==0){
                return target/arr[0];
            }else{
                return INF;
            }
        }
        if(dp[i][target]!=-1){
            return dp[i][target];
        }
        int take=INF;
        int nottake=mincoin(dp,arr, i-1, target);

        if(target>=arr[i]){
            take=1+mincoin(dp,arr, i, target-arr[i]);
        }
        dp[i][target]=Math.min(take,nottake);
        return Math.min(take,nottake);
    }
    public int coinChange(int[] coins, int amount) {
        int[][] dp=new int[coins.length][amount+1];
        for(int[] row:dp){
            Arrays.fill(row,-1);
        }
        int res=mincoin(dp,coins,coins.length-1,amount);
        return (res==INF)?-1:res;
    }
}


