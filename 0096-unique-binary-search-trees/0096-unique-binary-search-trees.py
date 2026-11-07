class Solution:
    def numTrees(self, n: int) -> int:
        # catalan formula
        # every combination of left subtre * combination of right subtree
        def factorial(n):
            if n==0 or n==1:
                return 1

            return n*factorial(n-1)

        return factorial(2*n)//((factorial(n+1))*(factorial(n)))        



        