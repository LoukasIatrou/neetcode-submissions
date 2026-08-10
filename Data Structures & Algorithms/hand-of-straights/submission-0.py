class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        if (len(hand))%groupSize!=0:
            return False
        remaining = (len(hand))/groupSize
        for h in hand:
            count[h] = count.get(h,0) + 1
        while remaining:
            handMin = min(count)
            for i in range(handMin,handMin+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] ==0:
                    del count[i]
            remaining -= 1
        return True if remaining == 0 else False
    
        
            