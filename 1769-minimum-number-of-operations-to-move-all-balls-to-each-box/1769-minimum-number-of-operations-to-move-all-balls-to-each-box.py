class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            diff = 0
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    diff+=abs(i-j)

            ans[i] = diff

        return ans            
        