class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_dict = {}

        for ele in s:
            value = temp_dict.setdefault(ele, 0)
            temp_dict[ele] = value+1;
        
        for ele in t:
            value = temp_dict.setdefault(ele, 0)
            temp_dict[ele] = value-1;

        return all(value == 0 for value in temp_dict.values())
        