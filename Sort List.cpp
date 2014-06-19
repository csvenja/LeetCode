#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getLast(ListNode *head, int n) {
        int i = 1;
        while (i < n && head->next != NULL) {
            head = head->next;
            i++;
        }
        return head;
    }
    ListNode *getEnd(ListNode *head) {
        while (head->next != NULL) {
            head = head->next;
        }
        return head;
    }
    ListNode *merge(ListNode *p1, ListNode *p2) {
        if (!p1) {
            return p2;
        }
        if (!p2) {
            return p1;
        }
        ListNode *head = NULL;
        if (p1->val < p2->val) {
            head = p1;
            p1 = p1->next;
        }
        else {
            head = p2;
            p2 = p2->next;
        }
        ListNode *current = head;
        while (p1 && p2) {
            if (p1->val < p2->val) {
                current->next = p1;
                p1 = p1->next;
            }
            else {
                current->next = p2;
                p2 = p2->next;
            }
            current = current->next;
        }
        if (p1) {
            current->next = p1;
        }
        else {
            current->next = p2;
        }
        return head;
    }
    ListNode *sortList(ListNode *head) {
        int n = 0;
        ListNode *current = head;
        while (current) {
            n++;
            current = current->next;
        }
        for (int step = 1; step < n; step *= 2) {
            ListNode *start = head;
            ListNode *before_p1 = NULL;
            while (start) {
                ListNode *p1 = start;
                ListNode *last_p1 = getLast(p1, step);
                if (!(last_p1->next))
                {
                    break;
                }
                ListNode *p2 = last_p1->next;
                last_p1->next = NULL;
                ListNode *last_p2 = getLast(p2, step);
                ListNode *after_p2 = last_p2->next;
                last_p2->next = NULL;

                p1 = merge(p1, p2);
                ListNode *end = getEnd(p1);

                end->next = after_p2;
                if (!before_p1)
                {
                    head = p1;
                }
                else {
                    before_p1->next = p1;
                }
                before_p1 = end;
                start = after_p2;
            }
        }
        return head;
    }
};

using namespace std;
int main(int argc, char *argv[]) {
    ListNode *p1 = new ListNode(6);
    ListNode *p2 = new ListNode(5);
    ListNode *p3 = new ListNode(4);
    ListNode *p4 = new ListNode(3);
    ListNode *p5 = new ListNode(2);
    ListNode *p6 = new ListNode(1);
    p1->next = p2;
    p2->next = p3;
    p3->next = p4;
    p4->next = p5;
    p5->next = p6;
    Solution *result = new Solution();
    ListNode *ans = result->sortList(p1);
    while (ans) {
        printf("%d\n", ans->val);
        ans = ans->next;
    }
}