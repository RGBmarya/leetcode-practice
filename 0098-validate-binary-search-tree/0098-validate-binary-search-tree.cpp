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

// valid tree: left subtree sorted, right subtree sorted, root is between max of left and min of right
class Solution {
public:
    TreeNode *min_of_tree(TreeNode *root) {
        if (root && root->left) {
            return min_of_tree(root->left);
        }
        return root;
    }
    
    TreeNode *max_of_tree(TreeNode *root) {
        if (root && root->right) {
            return max_of_tree(root->right);
        }
        return root;
    }
    
    bool isValidBST(TreeNode* root) {
        if (!root) {
            return true;
        }
        bool root_sorted = true;
        if (root->left) {
            root_sorted = root->val > max_of_tree(root->left)->val;
        }
        if (root_sorted && root->right) {
            root_sorted = root->val < min_of_tree(root->right)->val;
        }
        return root_sorted && isValidBST(root->left) && isValidBST(root->right);
    }
};