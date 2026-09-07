class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
            
            if seen[num] > 1:
                return True

        return False
