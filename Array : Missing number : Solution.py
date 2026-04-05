# Promblem - Missing Number 
# Appraoch - Sum formula 
# Time and space complexity - O(n) & O(1)
# Leetcode - 268
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();

        int total = n * (n+1) / 2;

        int sum = 0;
        for(int num : nums) {
            sum += num;
        }
        return total - sum;
    }
};
