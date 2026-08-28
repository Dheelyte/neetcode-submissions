class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # IMPLEMENTATION 1
        # 1. get the length of the list
        # 2. convert list to set
        # 3. get the length of the set
        # 4. compare the lengths: if lengths are unequal,
        # then a duplicate element was present

        # list_length = len(nums)
        # set_length = len(set(nums))
        # return list_length != set_length

        # IMPLEMENTATION 2
        # initialize an empty set
        # for each element in list, if element is in set,
        # return True, else add the element to the set
        # return False after the loop because no True was 
        # returned

        seen = set()
        for elem in nums:
            if elem in seen:
                return True
            seen.add(elem)
        return False