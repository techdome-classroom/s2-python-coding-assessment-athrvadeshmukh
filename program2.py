class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their integer values
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Variable to store the final integer value
        total = 0
        
        # Traverse the Roman numeral string
        for i in range(len(s)):
            # If the current value is less than the next value, subtract it
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            else:
                # Otherwise, add it to the total
                total += roman_values[s[i]]
        
        return total
