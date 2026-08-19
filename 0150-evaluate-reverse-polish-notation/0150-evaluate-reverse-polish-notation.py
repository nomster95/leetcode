class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i=="+":
                stack.append(stack.pop()+stack.pop())
            elif i=="-":
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif i=="*":
                a,b = stack.pop(),stack.pop()
                stack.append(b*a)
            elif i=="/":
                a,b = stack.pop(),stack.pop() 
                result = abs(b)//abs(a)
                if (a<0) != (b<0):
                    result = -result
                stack.append(result)
            else:
                stack.append(int(i))    

        return stack[0]        

        
                
        