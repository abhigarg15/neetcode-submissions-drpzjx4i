class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Method1: we will create a dictionary, where the key would be the sorted first instance in
        list and value would be the element itself.
        """

        d = {}

        for s in strs:
            ele = ''.join(sorted(s))
            if ele in d:
                d[ele].append(s)
            else:
                d[ele] = [s]

        ans = []
        for key, values in d.items():
            ans.append(values)

        return ans
