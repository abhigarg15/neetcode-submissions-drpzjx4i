class Solution {
public:
    bool isPalindrome(string s) {
        std::string t;
        for (auto i : s){
            if (isalnum(i))
                t += tolower(i);
        }
        string x = t;
        reverse(x.begin(),x.end());
        return t == x;
    }
};
