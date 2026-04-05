class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Method1: we will create a dictionary, where the key would be the sorted first instance in
        list and value would be the element itself.
        TC = O(n*klogk) : n is number of strings and k is the lenght of longest string
        SC = O(n*k)
        """

        # d = {}

        # for s in strs:
        #     ele = ''.join(sorted(s)) # critical factor, sorted returns list of sorted elements in 
        #     # string
        #     if ele in d:
        #         d[ele].append(s)
        #     else:
        #         d[ele] = [s]

        # ans = []
        # for key, values in d.items():
        #     ans.append(values)

        # return ans

        """
        Method2: 
        """

        # res = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)

        # return list(res.values())

        track = defaultdict(list)
        for i in strs:
            track["".join(sorted(i))].append(i)
        res = []
        for key, val in track.items():
            res.append(val)

        return res
