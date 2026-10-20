class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        freq = {}
        ans = {}
        jumbled = []

        for i in range(len(mapping)):
            freq[i] = mapping[i]

        for index,val in enumerate(nums):
            new_num = ""
            for k in str(val):
                x = int(k)
                new_num+= str(freq[x])

            converted = int(new_num)
            jumbled.append((converted,index,val))

        jumbled.sort()
        final = []
        for item in jumbled:
            final.append(item[2])

        return final            




           




            
        