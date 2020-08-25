# Time Complexity : O(n^3) 
# Space Complexity :O(n^2)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Your code here along with comments explaining your approach
class Solution:
    def maxCoins(self, nums):
        if len(nums) == 0:
            return 0 
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for ln in range(1, n+1):
            for i in range(0, n-ln+1):
                j = i + ln - 1 
                
                for k in range(i, j+1): # for the subarray i to j 
                    left, right = 1, 1 
                    if j != n-1:
                        right = nums[j+1]
                    
                    if i != 0:
                        left = nums[i-1]
                    
                    before, after = 0 ,0 
                    if k != i:
                        before = dp[i][k-1]
                    
                    if k != j:
                        after = dp[k+1][j]
                    
                    dp[i][j] = max(dp[i][j], before + left*nums[k]*right + after)

        return dp[0][n-1]
                        
if __name__ == "__main__":
    s = Solution()
    res = s.maxCoins([3,1,5,8])
    assert res == 167