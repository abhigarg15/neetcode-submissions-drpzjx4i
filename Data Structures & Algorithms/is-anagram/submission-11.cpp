class Solution {
public:
    bool isAnagram(string s, string t) {
        
        // sort(s.begin(), s.end()); 
        // sort(t.begin(),t.end());
        // return s == t;


        // so sorting will take nlog(n) complexity, we can do it
        // in O(n)

        unordered_map<int,int> mp;
        for(auto i:s)
            mp[i]++;

        for(auto i:t)
            mp[i]--;

        for (auto [key,value]:mp)
            if (value != 0)
                return false;
        
        return true;
    }
};
