# Promblem - Container with most water
# Approach - Two pointers
# Time and space complexity - O(n) & O(1) 
# Leetcode and Diffculty - 11 & Medium
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxWater = 0;
        int lp = 0; int rp = height.size()-1;

        while(lp < rp) {
            int w = rp - lp;
            int ht = min(height[lp], height[rp]);
            int currWater = w * ht;
            maxWater = max(maxWater, currWater);

            height[lp] < height[rp] ? lp++ : rp--;
        }
        
        return maxWater;
    }
};
