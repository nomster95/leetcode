class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip()
        lst = word.split()
        lst.reverse()
        return len(lst[0])

        