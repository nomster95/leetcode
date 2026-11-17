class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = [0]*len(queries)
        vowels = {'a','e','i','o','u'}

        vowel_count = [0]*len(words)
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                vowel_count[i] = 1

        prefix_v = [0]*(len(words))
        prefix_v[0] = vowel_count[0]    
        for i in range(1,len(words)):
            prefix_v[i] = prefix_v[i-1] + vowel_count[i]

        final_prefix = [0] + prefix_v
        ans = [0]*len(queries)
        for x in range(len(queries)):
            l = queries[x][0]
            r = queries[x][1]
            ans[x] = final_prefix[r+1] - final_prefix[l]

        return ans    





