class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        oc,cc = n,n
        def backtrack(oc,cc):
            if oc == 0 and cc == 0:
                res.append("".join(temp))
                return 
            if oc>0:
                temp.append("(")
                backtrack(oc-1,cc)
                temp.pop()
            if cc>oc:
                temp.append(")")
                backtrack(oc,cc-1)
                temp.pop()
        backtrack(n,n)
        return res
   