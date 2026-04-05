class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key = lambda x: x[0])

        stack = []

        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                prevStart, prevEnd = stack.pop()
                newStart = min(prevStart,interval[0])
                newEnd = max(prevEnd,interval[1])
                stack.append([newStart,newEnd])
            else:
                stack.append(interval)

        return stack
