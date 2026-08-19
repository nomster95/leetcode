class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        stack = []
        for i in range(1,n+1):
            if len(stack)==len(target):
                break
            if i in target:
                stack.append(i)
                ans.append("Push")
            else:
                ans.append("Push") 
                ans.append("Pop") 

        return ans          
            

       
    
        
        