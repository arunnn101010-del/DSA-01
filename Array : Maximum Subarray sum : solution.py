# promblem - Maximum Subarray sum 
# Apporach - Brute force approach 
# time and space complexity - O(n^2) & O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum  = INT_MIN;
        int currSum = 0;

        for(int i=0; i<nums.size(); i++) {
            currSum += nums[i];
            maxSum = max(maxSum, currSum);

            if(currSum < 0) {
                currSum = 0;
            }
        }
        return maxSum;
    }
};
