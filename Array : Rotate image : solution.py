# Prombelm - Rotate image 
# Approach - transpose + reverse 
# Time and space complexity - O(n^2) & O(1)
# Leetcode and diffculty level - 48 & medium 
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        for(int i=0; i<n; i++) {
            for(int j=i; j<n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        for(int i=0; i<n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
