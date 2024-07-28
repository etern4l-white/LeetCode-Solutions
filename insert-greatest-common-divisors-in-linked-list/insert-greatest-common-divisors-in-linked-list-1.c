/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int gcd(int a, int b){
    return a==0?b:gcd(b%a, a);
}
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head){
    struct ListNode* orghead = head;
    while(head->next){
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = gcd(head->val, head->next->val);
        node->next = (head->next);
        head->next = (node);
        head = head->next->next;
    }
    return orghead;
}
