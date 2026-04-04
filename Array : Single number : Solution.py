#  promblem - Single number
# Approach - Bit manipulation
# Time and space complexity - O(n) & O(1)
# Leetcode - 136
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;

        for(int i = 0; i < nums.size(); i++) {
            ans ^= nums[i];
        }
        return ans;
    }
};
