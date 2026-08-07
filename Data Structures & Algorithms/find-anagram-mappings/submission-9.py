class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = {}

        for idx, num in enumerate(nums2):
            indexes[num] = idx
        
        return [indexes[num] for num in nums1]