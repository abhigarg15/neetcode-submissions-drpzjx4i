class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // lets try through sorting nlog(n)
        if (!nums.size())
            return false;
        sort(nums.begin(), nums.end());

        for ( int i{0}; i < nums.size()-1; i++){
            if (nums[i] == nums[i+1])
                return true;
        }

        return false;
        // unordered_map<int,int> mp;

        // for ( const auto& num : nums){
        //     if (mp.find(num) != mp.end())
        //         return true;
        //     else{
        //         mp[num]++;
        //     }
        // }
        // return false;
        // if (!nums.size()){
        //     return false;
        // }

        // sort(nums.begin(),nums.end());

        // for (int i = 0 ; i < nums.size()-1 ; i++){
        //     if ( nums[i] == nums[i+1]){
        //         return true;
        //     }
        // } 
        // return false;

    }
};
