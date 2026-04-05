class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;

        for (const auto& num:nums)
            mp[num]++;

        vector<pair<int,int>> v;

        for (const auto& p: mp){
            v.push_back({p.second,p.first});
        }

        sort(v.rbegin(), v.rend());

        vector<int> ans;

        for (auto&i : v){
            ans.push_back(i.second);
            k--;
            if (k == 0)
                break;
        }
        return ans;
    }
};
