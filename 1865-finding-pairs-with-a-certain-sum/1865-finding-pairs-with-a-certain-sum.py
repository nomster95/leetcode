class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = {}
        for x in self.nums2:
            if x not in self.freq:
                self.freq[x] = 1
            else:
                self.freq[x]+=1  
        

    def add(self, index: int, val: int) -> None:
        if index<=len(self.nums2)-1:
            self.freq[self.nums2[index]]-=1
            if self.freq[self.nums2[index]]==0:
                del self.freq[self.nums2[index]]

            self.nums2[index]+=val
            if self.nums2[index] not in self.freq:
                self.freq[self.nums2[index]] = 1
            else:
                self.freq[self.nums2[index]]+=1    

        

    def count(self, tot: int) -> int:
        count = 0

        for i in self.nums1:
            if tot-i in self.freq:
                count+=self.freq[tot-i]


        return count        


        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)