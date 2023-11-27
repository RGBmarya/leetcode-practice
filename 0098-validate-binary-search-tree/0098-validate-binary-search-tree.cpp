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


//base case: if root == nullptr, return true
//recursive step: 
// if left substree exists, root node must be greater than max of left subtree
// if right subtree exists, root node less than min of right subtree
// left and right subtrees valid
class Solution {
public:
    int min_of_tree(TreeNode* root) {
        if (!root->left) {
            return root->val;
        }
        return min_of_tree(root->left);
    }
    
    int max_of_tree(TreeNode* root) {
        if (!root->right) {
            return root->val;
        }
        return max_of_tree(root->right);
    }
    
    bool isValidBST(TreeNode* root) {
        if(!root) {
            return true;
        }
        bool root_valid = true;
        if (root->left) {
            root_valid = root->val > max_of_tree(root->left);
        }
        if (root_valid && root->right) {
            root_valid = root->val < min_of_tree(root->right);
        }
        
        return root_valid && isValidBST(root->left) && isValidBST(root->right);
    }
};