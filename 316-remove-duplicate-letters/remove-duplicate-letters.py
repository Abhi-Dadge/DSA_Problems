class Solution(object):
    def removeDuplicateLetters(self, s):
        lst = {}
        for i, ch in enumerate(s):
            lst[ch] = i
        stack = []
        seen = set()
        
        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and ch < stack[-1] and lst[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)
        return "".join(stack)

         