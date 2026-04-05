class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        ans = strs[0]

        for i in range(1,len(strs)):
            temp = ""
            x = min(ans,strs[i])

            for j in range(len(x)):
                if ans[j] == strs[i][j]:
                    temp += ans[j]
                else:
                    break

            ans = temp

        return ans
                
            