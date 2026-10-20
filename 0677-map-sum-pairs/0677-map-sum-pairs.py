class MapSum:

    def __init__(self):
        self.freq = {}
        

    def insert(self, key: str, val: int) -> None:
        self.freq[key] = val
        
        
        

    def sum(self, prefix: str) -> int:
        ans = 0
        for x in self.freq:
            if x.startswith(prefix):
                ans+=self.freq[x]

        return ans        

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)