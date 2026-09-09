class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n<10**6:
            return n-1000 + 1
        elif n<10**9:
            one_comma = 999999 - 1000 + 1
            two_comma = n - 10**6 + 1
            return one_comma + 2 * two_comma

        elif n < 10**12:
            one_comma = 999999 - 1000 + 1
            two_comma = 999999999 - 10**6 + 1
            three_comma = n - 10**9 + 1
            return one_comma + 2 * two_comma + 3 * three_comma        

        elif n < 10**15:
            one_comma = 999999 - 1000 + 1
            two_comma = 999999999 - 10**6 + 1
            three_comma = 999999999999 - 10**9 + 1
            four_comma = n - 10**12 + 1

            return one_comma + 2 * two_comma + 3 * three_comma + 4 * four_comma    

        else:
            one_comma = 999999 - 1000 + 1
            two_comma = 999999999 - 10**6 + 1
            three_comma = 999999999999 - 10**9 + 1
            four_comma = 10**15 - 10**12
            return one_comma + 2 * two_comma + 3 * three_comma + 4 * four_comma + 5
            

        