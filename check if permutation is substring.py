class Solution:
    def search(self, txt, pat):
        n, m = len(txt), len(pat)
        
        if m > n:
            return False
        
        # Frequency arrays for pat and current window
        count_pat = [0] * 26
        count_txt = [0] * 26
        
        # Fill initial counts
        for i in range(m):
            count_pat[ord(pat[i]) - ord('a')] += 1
            count_txt[ord(txt[i]) - ord('a')] += 1
        
        # Check first window
        if count_pat == count_txt:
            return True
        
        # Slide the window
        for i in range(m, n):
            # Add new character
            count_txt[ord(txt[i]) - ord('a')] += 1
            
            # Remove old character
            count_txt[ord(txt[i - m]) - ord('a')] -= 1
            
            # Compare
            if count_pat == count_txt:
                return True
        
        return False
