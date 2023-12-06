/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// for tree to be valid, LEFT subtree has to be valid, RIGHT subtree has to be vaild, 
// root has to be greater than max of LEFT (if exists) AND root has to be less than min of right (if exists)
// base case: if node == nullptr, then valid
// if 
// recursive step: 
class Solution {
public:
    TreeNode* max_of_tree(TreeNode *root) {
        if (root->right) {
            return max_of_tree(root->right);
        }
        return root; 
    }
    
    TreeNode* min_of_tree(TreeNode *root) {
        if(root->left) {
            return min_of_tree(root->left);
        }
        return root;
    }
    
    bool isValidBST(TreeNode* root) {
        if (!root) {
            return true;
        }
        
        bool root_valid = true;
        if (root->left) {
            root_valid = root->val > max_of_tree(root->left)->val;
        }
        if (root_valid && root->right) {
            root_valid = root->val < min_of_tree(root->right)->val;
        }
        
        return root_valid && isValidBST(root->left) && isValidBST(root->right);
    }
};