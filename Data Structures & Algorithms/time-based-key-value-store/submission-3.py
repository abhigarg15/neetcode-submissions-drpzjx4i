class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp[key]

        low = 0
        high = len(arr)-1
        res = ""
        if not arr:
            return ""

        if timestamp >= arr[-1][1]:
            return arr[-1][0]

        while low<=high:
            mid = (low + high)//2

            if arr[mid][1] == timestamp:
                return arr[mid][0]
            
            elif arr[mid][1] < timestamp:
                res = arr[mid][0]
                low = mid+1
            else:
                high = mid-1

        return res
