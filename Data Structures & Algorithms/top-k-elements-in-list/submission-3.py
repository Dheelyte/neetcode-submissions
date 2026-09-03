class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1

        sorted_s = sorted(res.items(), key=lambda item: item[1], reverse=True)
        return [i[0] for i in sorted_s][:k]