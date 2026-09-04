class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        for i in nums:
            has[i] = has.get(i,0) + 1
        return sorted(has,key = has.get,reverse=True)[:k]
        