class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = defaultdict(int)
        def rec(i):
            if i == len(s):
                return True

            if i in cache:
                return cache[i] 

            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] in wordDict:
                    if rec(i+len(w)):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        return rec(0)