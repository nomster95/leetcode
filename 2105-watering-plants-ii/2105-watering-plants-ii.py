class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        refills = 0
        n = len(plants)
        a = 0
        b = n-1
        fullA = capacityA
        fullB = capacityB

        while a<b:
            if capacityA<plants[a]:
                refills+=1
                capacityA = fullA

            if capacityB<plants[b]:
                refills+=1
                capacityB = fullB 

            capacityA-=plants[a]
            a+=1
            capacityB-=plants[b]
            b-=1

        if a==b:
            if max(capacityA,capacityB)<plants[a]:
                refills+=1   


        return refills    



