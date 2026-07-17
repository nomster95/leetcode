class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        net = s+s
        if(len(s)!=len(goal)):
            return False
            
        if(goal in net):
            return True
        
        return False