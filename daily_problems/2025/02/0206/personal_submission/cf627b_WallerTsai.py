class Solution:
    def __init__(self,n:int,fixing_time:int,pre_eff:int,eff:int) -> None:
        self.order = [0] * n
        self.fix = fixing_time
        self.pre_eff = pre_eff
        self.eff = eff

    def update(self,day:int,size:int) -> None:
        self.order[day-1] += size

    def out(self,day:int) -> None:
        ans = 0

        for i in range(day-1):
            ans += min(self.order[i],self.pre_eff)

        for j in range(day-1+self.fix,len(self)):
            ans += min(self.order[j],self.eff)

        print(ans)

    def __len__(self):
        return len(self.order)
    
if __name__ == "__main__":
    n, k, a, b, q = map(int, input().split())
    fun = Solution(n,k,b,a)
    for _ in range(q):
        _input = list(map(int,input().split()))

        if _input[0] == 1:
            fun.update(_input[1],_input[2])
        else:
            fun.out(_input[1])
