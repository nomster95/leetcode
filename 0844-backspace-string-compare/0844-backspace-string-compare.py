class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for i in list(s):
            if(i!='#'):
                s1.append(i)
            elif(len(s1)>0):
                s1.pop() 
        for i in list(t):
            if(i!='#'):
                t1.append(i)
            elif(len(t1)>0):
                t1.pop()            
        
        return s1 == t1