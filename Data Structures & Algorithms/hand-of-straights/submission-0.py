from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # A quick check: if the total cards aren't divisible by groupSize, it's impossible
        if len(hand) % groupSize != 0:
            return False
            
        # Count frequencies
        count = Counter(hand)
        
        # Sort the unique card values
        sorted_keys = sorted(count.keys())
        
        for num in sorted_keys:
            # While this card still has a count, try to build a group
            while count[num] > 0:
                for i in range(groupSize):
                    # Check if the consecutive card exists and has available count
                    if count[num + i] > 0:
                        count[num + i] -= 1
                    else:
                        # Cannot form a consecutive group
                        return False
        
        return True