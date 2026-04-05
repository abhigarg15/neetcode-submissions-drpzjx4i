class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        stack = []
        for interval in intervals:
            start,end = interval
            if stack and stack[-1][1] >= start:
                stack[-1][1] = max(end,stack[-1][1])
            else:
                stack.append(interval)
        
        return stack
            