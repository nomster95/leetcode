class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = i

        for j in range(len(operations)):
            nums[freq[operations[j][0]]] = operations[j][1]
            freq[operations[j][1]] = freq[operations[j][0]]
            del freq[operations[j][0]]

        return nums       
            
                

        