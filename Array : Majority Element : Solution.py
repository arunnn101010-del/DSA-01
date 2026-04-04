# promblem - Array Majority Elemnt 
# Approach - Moore's Voting Algorithm
# Time and space complexity - O(n) & O(1)
# Leetcode - 169
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int freq = 0, ans = 0;

        for(int i=0; i < nums.size(); i++) {
            if(freq == 0) {
                ans = nums[i];
            }
            if(ans == nums[i]) {
                freq++;
            } else {
                freq--;
            }
        }
        return ans;
    }
};
