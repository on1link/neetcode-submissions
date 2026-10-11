class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        return sorted(nums, key=lambda x: (seen[x], -x))
        