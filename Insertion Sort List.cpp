#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *insertionSortList(ListNode *head) {
        ListNode *pre_head = new ListNode(0);
        ListNode *p = pre_head;
        ListNode *current = head;
        while (current) {
            p = pre_head;
            while (p->next && p->next->val < current->val) {
                p = p->next;
            }
            ListNode *tmp = current->next;
            current->next = p->next;
            p->next = current;
            current = tmp;
        }
        return pre_head->next;
    }
};

using namespace std;
int main(int argc, char *argv[]) {
    Solution *result = new Solution();
    ListNode *a = new ListNode(5);
    ListNode *b = new ListNode(4);
    ListNode *c = new ListNode(3);
    ListNode *d = new ListNode(2);
    ListNode *e = new ListNode(1);
    a->next = b;
    b->next = c;
    c->next = d;
    d->next = e;
    ListNode *ans = result->insertionSortList(a);
    while (ans) {
        printf("%d\n", ans->val);
        ans = ans->next;
    }
}