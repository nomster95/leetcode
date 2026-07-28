class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        nums = []
        n = len(words)
        for i in range(n):
            if x in words[i]:
                nums.append(i)

        return nums        
        