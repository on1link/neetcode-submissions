class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        seen = defaultdict(int)

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
                
        for key, value in seen.items():
            if value % 2 != 0:
                return False

        return True 