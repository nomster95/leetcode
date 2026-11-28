class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word]+=1

        max_len = 0
        max_p = 0
        for ch in freq:
            if ch==ch[::-1]:
                pair = freq[ch]//2
                max_len+=len(ch)*pair*2

                if freq[ch]%2==1:
                    max_p = 2 
                    
            else:
                if ch<ch[::-1] and ch[::-1] in freq:
                    mul = min(freq[ch],freq[ch[::-1]])
                    max_len+=(len(ch)*mul*2)


        return max_len + max_p                        

        