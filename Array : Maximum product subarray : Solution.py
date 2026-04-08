# Promblem - Maximum product subarray 
# Approach - Dynamic programming 
# Time and space complexity - O(n) & O(1)
# Leetcode and diffculty level  - 152 & medium
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int currMax = nums[0];
        int currMin = nums[0];
        int ans = nums[0];

        for(int i = 1; i < nums.size(); i++) {
            int temp = currMax;

            currMax = max({nums[i], nums[i]*currMax, nums[i]*currMin});
            currMin = min({nums[i], nums[i]*temp, nums[i]*currMin});

            ans = max(ans, currMax);
        }
        return ans;
    }
};
