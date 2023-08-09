class Solution:
    def replaceDigits(self, s: str) -> str:
        alp = str(string.ascii_lowercase)
        res = ""
        for i in range(0, len(s)) :
            if i % 2 != 0 :
                print(alp.find(s[i - 1]))
                res += alp[(alp.find(s[i - 1]) + int(s[i]))]
            else :
                res += s[i]
                
        
        return res