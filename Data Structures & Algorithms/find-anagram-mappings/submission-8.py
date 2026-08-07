class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = {}
        result = []

        for num in nums1:
            for idx, val in enumerate(nums2):
                if num == val:
                    indexes[val] = idx

        for num in nums1:
            if num in indexes.keys():
                result.append(indexes[num])
        
        return result