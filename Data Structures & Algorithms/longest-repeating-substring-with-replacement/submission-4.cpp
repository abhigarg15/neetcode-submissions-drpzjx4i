class Solution {
public:
    int characterReplacement(string s, int k) {
        
        // we need to give the longest window as output
        // brute force approach is O(n^2)

        unordered_map<int,int> count;
        int res = 0;

        int l = 0 ; 
        int maxFrequency = 0;

        for (int r = 0 ; r < s.size() ; r++){
            count[s[r]]++;
            maxFrequency = max(maxFrequency, count[s[r]]);

            while ((r - l + 1) - maxFrequency > k){
                count[s[l]]--;
                l++;
            }

            res = max(res, r-l+1);
        }


        return res;
    }
};
