class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        opening = 0
        closed = 0
        for i in s:
            if i=="(":
                opening+=1     
            elif i==")":
                closed+=1
            

            ans.append(i)
            if closed>opening:
                ans.pop()
                closed-=1

        opening = 0
        closed = 0  
        f_ans = []      

        for i in range(len(ans)-1,-1,-1):  
            if ans[i]=="(":
                opening+=1 
            elif ans[i]==")":
                closed+=1

            f_ans.append(ans[i])

            if opening>closed:
                f_ans.pop()
                opening-=1

        final =  "".join(f_ans)    
        return final[::-1]        




            

            

                       
        
        