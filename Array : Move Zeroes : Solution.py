# Promblem - Move Zeroes 
# Approach - Optimal Approach 
# Time and space complexity - O(n) & O(1)
# Leetcode - 283
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
