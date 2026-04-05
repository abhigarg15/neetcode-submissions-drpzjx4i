class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = sorted(s1)
        # for i in range(len(s2)-len(s1)+1):
        #     tmp = sorted(s2[i:i+len(s1)])
        #     # print(tmp)
        #     if s1 == tmp:
        #         return True

        # return False
        if len(s1) > len(s2):
            return False
        mp = Counter(s1)
        tmpTracker = {}
        for i in range(len(s1)):
            tmpTracker[s2[i]] = 1 + tmpTracker.get(s2[i],0)

        if mp == tmpTracker:
            return True

        for i in range(len(s1),len(s2)):
            tmpTracker[s2[i]] = 1 + tmpTracker.get(s2[i],0)
            tmpTracker[s2[i - len(s1)]]-=1
            if tmpTracker[s2[i - len(s1)]] == 0:
                del tmpTracker[s2[i - len(s1)]]
            
            if tmpTracker == mp:
                return True
        
        return False



