# promblem - Maximum Subarray sum 
# Apporach - Brute force approach 
# time and space complexity - O(n^2) & O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int maxSum  = INT_MIN;

        for(int st = 0; st < n; st++) {
            int currSum = 0;

            for(int end = st; end < n; end++) {
                currSum += nums[end];
                maxSum = max(maxSum, currSum);
            }
        }
        return maxSum;
    }
};
