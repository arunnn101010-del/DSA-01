# Promblem - Move Zeroes 
# Approach - Optimal Approach 
# Time and space complexity - O(n) & O(1)
# Leetcode & DIffculty - 283 & Easy
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;

        for(int j = 0; j < nums.size(); j++) {
            if(nums[j] != 0) {
                swap(nums[j], nums[i]);
                i++;
            }
        }
    }
};
