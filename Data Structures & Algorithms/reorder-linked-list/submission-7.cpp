/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* fast = head->next;
        ListNode* slow = head;

        while ( fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode* prev = nullptr;
        ListNode* second = slow->next;
        slow->next = nullptr;

        while (second){
            ListNode* temp = second->next;
            second->next = prev;

            prev = second;

            second = temp;
        }
        
        // second is now destroyed
        
        ListNode* first = head;
        second = prev;
        
        while ( second){
            ListNode* temp = first->next;
            ListNode* temp2 = second->next;

            first->next = second;
            second->next = temp;

            first = temp;
            second = temp2;
        }
    }
};
