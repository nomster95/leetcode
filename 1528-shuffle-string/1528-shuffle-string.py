class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle = [' ']*len(indices)
        for i in range(len(indices)):
            shuffle[indices[i]] = s[i]
        

        return "".join(shuffle)