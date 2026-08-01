class TimeMap:

    def __init__(self):
        self.store = {} #key  list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] #create new list for key if not in list
        self.store[key].append([value, timestamp]) #append params to list

    def get(self, key: str, timestamp: int) -> str:
        #intialize
        res = ""
        values = self.store.get(key, [])

        # binary search
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r ) // 2
            if values[mid][1] <= timestamp: #valid timestamp
                res = values[mid][0] #update res
                l = mid + 1 #search right
            else: #invalid timestamp
                r = mid - 1

        return res
