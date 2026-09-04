class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            has = {}
            for i in nums:
                has[i] = has.get(i, 0) + 1

            return sorted(has,reverse=True,key=has.get)[:k]
        