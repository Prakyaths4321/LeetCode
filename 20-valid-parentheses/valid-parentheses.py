class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        st = []
        pair = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pair:
                if not st or st.pop() != pair[c]:
                    return False
            else:
                st.append(c)
        return not st