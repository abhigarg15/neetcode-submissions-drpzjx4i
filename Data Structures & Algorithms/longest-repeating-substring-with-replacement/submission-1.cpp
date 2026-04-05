class Solution {
public:
    int characterReplacement(string s, int k) {
        
        // we need to give the longest window as output
        // brute force approach is O(n^2)

        int res = 0;
        for ( int i = 0 ; i < s.size() ; i++){
            unordered_map<int,int> map ;
            int maxfrequency = 0;
            for ( int j = i ; j < s.size() ; j++){
                map[s[j]]++; // adding the frequency of the character to the hashmap
                maxfrequency = max(maxfrequency, map[s[j]]);

                if ( (j-i+1) - maxfrequency <= k){
                    res = max(res, j-i+1);
                } 
            }
        }

        return res;
    }
};
