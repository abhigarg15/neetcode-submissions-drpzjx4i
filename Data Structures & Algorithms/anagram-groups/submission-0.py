class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:

            temp = ''.join(sorted(i))
            print(temp)
            if temp in d :
                d[temp].append(i)   
                # d[sorted(i)].appned(i)
            else:
                d[temp] = [i]

        ans = []
        for key in d:
            ans.append(d[key])

        return ans
