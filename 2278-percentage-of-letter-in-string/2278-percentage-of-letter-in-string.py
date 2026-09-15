class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        marks = s.count(letter)
        return int((marks/len(s))*100)
        
        