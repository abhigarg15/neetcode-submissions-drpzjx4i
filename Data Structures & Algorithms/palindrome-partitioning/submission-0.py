class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.ans = []

        part = []

        def rec(i):
            if i >= len(s):
                self.ans.append(part[:])
                return

            for j in range(i,len(s)):
                if self.isPalin(s,i,j):
                    part.append(s[i:j+1])
                    rec(j+1)
                    part.pop()

        rec(0)
        return self.ans

    def isPalin(self, s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True    

        