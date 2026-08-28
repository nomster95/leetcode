class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for i in s:
            if i=="*":
                if len(result)!=0:
                    result.pop()
            elif i=="#":
                result+=result
            elif i=="%":
                result.reverse()
            else:
                result.append(i)

        return "".join(result)            

        
        