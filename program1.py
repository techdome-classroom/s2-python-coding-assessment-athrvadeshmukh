class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold matching pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the current closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets have been matched correctly
        return not stack
