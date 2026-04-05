class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        condition1 = condition2 = condition3 = False

        for i in range(len(triplets)):
            x = triplets[i][0]
            y = triplets[i][1]
            z = triplets[i][2]

            if x > target[0] or y > target[1] or z > target[2]:
                continue

            if x == target[0]:
                condition1 = True

            if y == target[1]:
                condition2 = True

            if z == target[2]:
                condition3 = True

            if condition1 and condition2 and condition3:
                return True

        return condition1 and condition2 and condition3