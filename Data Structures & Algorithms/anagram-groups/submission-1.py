class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for elem in strs:
            sorted_elem = "".join(sorted(elem))
            res[sorted_elem].append(elem)
        return list(res.values())