class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for i in words:
            splt = i.split(separator)
            for j in splt:
                if j!="":
                    ans.append(j)

        return ans    

        