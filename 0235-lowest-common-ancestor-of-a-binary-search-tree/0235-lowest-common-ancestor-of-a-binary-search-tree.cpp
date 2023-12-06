/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


// if cur node is greater than both p and q, need to go left
// if cur node is less than both p and q, need to go right
// if cur node is between p and q (inclusive), then return node
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        return root;
        // if ((p <= root->val && root->val <= q) || (q <= root->val && root->val <= p)) {
        //     return root;
        // }
    }
};