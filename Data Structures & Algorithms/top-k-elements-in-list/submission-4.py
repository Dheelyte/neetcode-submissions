# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res = defaultdict(int)
#         for num in nums:
#             res[num] += 1

#         sorted_s = sorted(res.items(), key=lambda item: item[1], reverse=True)
#         return [i[0] for i in sorted_s][:k]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res