class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string,vector<string> > v;

        for (const auto& str: strs){
            string temp = str;
            sort(temp.begin(),temp.end());
            if (v.find(temp) != v.end()){
                v[temp].push_back(str);
            }
            else{
                v[temp].push_back(str);
            }
        }
        vector<vector<string>> ans;
        for (const auto& [key,value]:v){
            ans.push_back(value);
        }

        return ans;
    }
};
