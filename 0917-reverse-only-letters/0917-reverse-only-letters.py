class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st = list(s)
        l,r= 0, len(st)-1
        while l<r:
            if not st[l].isalpha():
                l+=1
            elif not st[r].isalpha():    
                r-=1
            else:
                st[l],st[r] = st[r],st[l]
                l+=1
                r-=1

        return "".join(st)














