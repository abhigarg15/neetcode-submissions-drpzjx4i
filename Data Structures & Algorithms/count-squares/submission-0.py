class CountSquares:

    def __init__(self):
        self.mp = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts.append(tuple(point))
        self.mp[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px,py = point
        res = 0

        for x,y in self.pts:
            if abs(px-x) == abs(py-y) and px!=x and py!=y:
                res += self.mp[(x,py)] * self.mp[(px,y)] 

        return res

