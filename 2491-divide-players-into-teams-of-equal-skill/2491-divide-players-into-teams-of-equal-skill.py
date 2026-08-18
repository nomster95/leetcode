class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = []
        product_sum = 0
        skill.sort()
        l = 0
        r = len(skill)-1
        while l<r:
            ans.append(skill[l]+skill[r])
            product_sum+=skill[l]*skill[r]
            l+=1
            r-=1

        if len(set(ans))!=1:
            return -1

        return product_sum      

        