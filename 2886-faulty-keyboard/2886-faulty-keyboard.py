class Solution(object):
    def finalString(self, s):
        st = []
        for char in s:
            if char != 'i':
                st.append(char)  
            else:
                st.reverse()  
        return ''.join(st) 