class Solution(object):
    def defangIPaddr(self, address):
        ip=address.replace('.','[.]')
        return ip