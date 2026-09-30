class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l1,l2,r = 0,0,0
        max_len_T = 0
        max_len_F = 0
        trues = 0
        falses = 0
        while r<len(answerKey):
            if answerKey[r]=='T':
                trues+=1
            else:
                falses+=1

            while trues>k:
                if answerKey[l1]=='T':
                    trues-=1
                l1+=1

            while falses>k:
                if answerKey[l2]=='F':
                    falses-=1
                l2+=1

            if trues<=k:
                max_len_T = max(max_len_T,r-l1+1)

            if falses<=k:
                max_len_F = max(max_len_F,r-l2+1)

            r+=1    

        return max(max_len_T,max_len_F)                                    
        