'''
# Target:
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


# testcase1: ["flower","flow","flight"]
# testcase2: ["dog","racecar","car"]

'''

# %%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # initial result
        final_result = ""
        # sorting lists
        strs.sort()

        if len(strs) == 0:
            return final_result

        if len(strs) == 1:
            return strs[0]

        # iterate from second word of the list 
        for s in strs[1:]:
            # initial before every comparison
            result = ""
            # only check within the length of the first word
            for i in range(len(strs[0])):
                if strs[0][i] == s[i]:
                    result += strs[0][i]
                else:
                    break
            final_result = result
        
        return final_result
            
            


#%%
strs = ["dog","racecar","car"]
strs.sort()
print(strs)
print(len(strs))

test1 = Solution()
print("result = " , test1.longestCommonPrefix(strs))

# %%
