class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        // unordered_map<string,vector<string> > v;

        // for (const auto& str: strs){
        //     string temp = str;
        //     sort(temp.begin(),temp.end());    
        //     v[temp].push_back(str);

        // }
        // vector<vector<string>> ans;
        // for (const auto& [key,value]:v){
        //     ans.push_back(value);
        // }

        // return ans;
        unordered_map<string,vector<string>> v;
        for (const auto&s:strs){
            vector<int> count(26,0);
            for (auto c:s){
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for(int i = 1 ; i < 26 ; i++){
                key += "," + to_string(count[i]);
            }
            v[key].push_back(s);
        }
        vector<vector<string>> ans;
        for(const auto [key,val]:v)
            ans.push_back(val);

        return ans;
    }
};
