class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # ans = ""
        # for x,y in zip(word1,word2):
        #     ans+= x+y

        # return ans

        i,j= 0,0
        ans = ""
        while i < len(word1) or j < len(word2):
            x = "" if  i >=len(word1) else word1[i]
            y = "" if  j >=len(word2) else word2[j]

            ans += x+y

            i+=1
            j+=1

        return ans