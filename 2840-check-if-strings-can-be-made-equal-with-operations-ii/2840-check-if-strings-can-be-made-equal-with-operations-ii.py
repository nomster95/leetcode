class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_pos1 = {}
        even_pos2 = {}
        odd_pos1 = {}
        odd_pos2 = {}
        for i in range(len(s1)):
            if i%2==0:
                if s1[i] not in even_pos1:
                    even_pos1[s1[i]]=1
                else:
                    even_pos1[s1[i]]+=1

                if s2[i] not in even_pos2:
                    even_pos2[s2[i]]=1
                else:
                    even_pos2[s2[i]]+=1

            else:
                if s1[i] not in odd_pos1:
                    odd_pos1[s1[i]]=1
                else:
                    odd_pos1[s1[i]]+=1

                if s2[i] not in odd_pos2:
                    odd_pos2[s2[i]]=1
                else:
                    odd_pos2[s2[i]]+=1


        if even_pos1==even_pos2 and odd_pos1==odd_pos2:
            return True

        return False                


                


        