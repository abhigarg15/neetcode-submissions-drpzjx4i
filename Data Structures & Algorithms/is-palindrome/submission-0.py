class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ''.join(filter(lambda x: x.isalnum(),s))
        # print(_s)
        return _s.lower() == _s[::-1].lower()