class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            occurence[num] = occurence.get(num, 0) + 1

        for num, occ in occurence.items():
            buckets[occ].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result