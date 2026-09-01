from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = defaultdict(int)
        for char in t:
            need[char] += 1
        chars_needed = set(t)
        total = len(chars_needed)

        window_counts = defaultdict(int)
        formed = 0
        l = 0
        len_ans = float('inf')
        subl, subr = 0, 0

        for r in range(len(s)):
            char = s[r]
            if char in chars_needed:
                window_counts[char] += 1
                if window_counts[char] == need[char]:
                    formed += 1

            while formed == total:
                cur_len = r - l + 1
                if cur_len < len_ans:
                    len_ans = cur_len
                    subl, subr = l, r + 1
                left_char = s[l]
                if left_char in chars_needed:
                    if window_counts[left_char] == need[left_char]:
                        formed -= 1
                    window_counts[left_char] -= 1
                l += 1

        return s[subl:subr] if len_ans != float('inf') else ""