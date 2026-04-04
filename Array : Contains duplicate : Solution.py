# Promblem - contains duplicate 
# Appraoch - Hashset
# Time and space complexit - O(n) & O(1)
# Leetcode - 217class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;

        for(int num : nums) {
            if(s.find(num) != s.end()) {
                return true;
            }
            s.insert(num);
        }
        return false;
    }
};
