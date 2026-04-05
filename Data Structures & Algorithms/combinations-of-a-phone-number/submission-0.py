class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mp = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        ans = []
        def rec(i,temp):
            if len(temp) == len(digits):
                ans.append(temp)
                return

            for k in mp[digits[i]]:
                rec(i+1,temp + k)
            


        rec(0,"")

        return ans