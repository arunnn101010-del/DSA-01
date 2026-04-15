# Promblem - 4 sum 
# Appraoch - 2 pointers + sorting
# Time complexity - O(n^3)
# Leetcode and diffculty level - 18 & medium
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int tar) {
        vector<vector<int>> ans;
        int n = nums.size();

        sort(nums.begin(), nums.end());

        for(int i=0; i<n; i++) {
            if(i > 0 && nums[i] == nums[i-1]) continue; // to avoid dupliacte value
            for(int j=i+1; j<n; j) {
                int p = j+1, q = n-1;

                while(p < q) {
                    long long sum = (long long)nums[i] + (long long)nums[j] 
                                    + (long long)nums[p] + (long long)nums[q];

                    if(sum < tar ) {
                        p++;
                    } else if(sum > tar) {
                        q--;
                    } else {
                        ans.push_back({nums[i], nums[j], nums[p], nums[q]});
                        p++; q--;

                        while(p < q && nums[p] == nums[p-1]) p++; // duplicate number
                    }
                }
                j++;
                while(j < n && nums[j] == nums[j-1]) j++; // skipping duplicate values
            }
        }
        return ans;
    }
};
