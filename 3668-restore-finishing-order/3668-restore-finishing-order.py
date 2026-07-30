class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        mates = set(friends)
        ans = []
        for i in order:
            if i in mates:
                ans.append(i)

        return ans        

        