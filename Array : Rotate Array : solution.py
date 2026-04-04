# Promblem - Rotate Array 
# Approach - Reversal Algorithm 
# Time and space complexity - O(n) & O(1)
# Leetcode - 189
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
      int n = nums.size();
      k = k % n;

      reverse(nums.begin(), nums.end());
      reverse(nums.begin(), nums.begin() + k);
      reverse(nums.begin() + k, nums.end());
    }
};
