/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int track(struct TreeNode* node, int l){
    if (!node){
        return l-1;
    }
    int l1, l2;
    l1 = track(node->left, l+1);
    l2 = track(node->right, l+1);
    return l1>l2?l1:l2;

}

int maxDepth(struct TreeNode* root) {
    int l = 1;
    if (!root){
        return 0;
    }
    int l1, l2;
    l1 = track(root->left, l+1);
    l2 = track(root->right, l+1);
    return l1>l2?l1:l2;
}
