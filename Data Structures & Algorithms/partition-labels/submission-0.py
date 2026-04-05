class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}

        for i,c in enumerate(s):
            lastIdx[c] = i


        res = []
        steps = 0
        end = 0
        for i,c in enumerate(s):
            steps+=1
            end = max(end,lastIdx[c])
            if i == end:
                res.append(steps)
                steps=0

        return res