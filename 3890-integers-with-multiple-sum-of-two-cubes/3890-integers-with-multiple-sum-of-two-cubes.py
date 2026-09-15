class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        seen = set()
        ans = set()

        limit = int(n ** (1 / 3)) + 1

        for a in range(limit):
            for b in range(a, limit):
                total = a**3 + b**3

                if total > n:
                    break

                if total in seen:
                    ans.add(total)
                else:
                    seen.add(total)

        return sorted(ans)
        