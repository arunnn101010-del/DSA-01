# Promblem - Trapping rain water 
# Appraoch - two pointers
# Time and space complexity - O(n) & O(1)
# Leetcode and diffculty level - 42 & hard
class solution {
public:
    int trap(vector<int>& height) {
    int n = height.size();
    int l = 0, r = n-1;
    int lmax = 0, rmax = 0;

    while(l < r) {
        lmax = max(lmax, heght[l]);
        rmax = max(rmax, height[r]);

        if( lmax < rmax) {
            ans += lmax - height[l];
            l++; 
        } else {
            ans += rmax - height[r];
            r--; 
        }
    }
    return ans;
  } 
};
