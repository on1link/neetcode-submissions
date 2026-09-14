class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        seen = defaultdict(int)

        for num in nums:
            if num not in seen:
                seen[num] = 0

            seen[num] += 1

        for count in seen.values():
            if count % 2 != 0:
                return False

        return True 