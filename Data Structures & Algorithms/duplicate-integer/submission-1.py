class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        cnt = cnt.most_common()
        return cnt[0][1] > 1 if nums else False    