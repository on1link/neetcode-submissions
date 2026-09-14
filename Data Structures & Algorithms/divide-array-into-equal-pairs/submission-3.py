class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        odd = set()

        for num in nums:
            if num not in odd:
                odd.add(num)
            else:
                odd.remove(num)

        return not len(odd) 