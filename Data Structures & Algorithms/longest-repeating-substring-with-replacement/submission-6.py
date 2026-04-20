class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        l, r = 0, 0 # Start r at 0 to include the first char properly
        track = {}
        max_len = 0
        most_freq = 0
        
        while r < len(s):
            # 1. Expand: Always add the current right character
            track[s[r]] = 1 + track.get(s[r], 0)
            
            # 2. Check validity
            most_freq = max(most_freq, track[s[r]])
            curr_len = r - l + 1
            
            if curr_len - most_freq <= k:
                # Valid window: move right to explore further
                max_len = max(max_len, curr_len)
                r += 1
            else:
                # Invalid window: shrink from left, then move right
                track[s[l]] -= 1
                l += 1
                r += 1 # Move r so we don't re-process the same char
                
        return max_len