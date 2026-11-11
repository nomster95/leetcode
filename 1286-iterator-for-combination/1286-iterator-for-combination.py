
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.k = combinationLength
        self.index = 0
        self.ans,self.sol = [] , []

        def backtrack(start):
            if len(self.ans)==self.k:
                self.sol.append(''.join(self.ans))
                return

            for i in range(start,len(characters)):
                self.ans.append(characters[i])

                backtrack(i+1)

                self.ans.pop()

        backtrack(0)            
        
    def next(self) -> str:
            x =  self.sol[self.index]
            self.index+=1
            return x


        

    def hasNext(self) -> bool:
        if self.index<len(self.sol):
            return True

        return False    
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()