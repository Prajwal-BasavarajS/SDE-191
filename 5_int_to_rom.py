class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of values to Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        roman = ""
        for i in range(len(val)):
            count = num // val[i]          # How many times the symbol fits
            roman += syms[i] * count      # Append that many symbols
            num -= val[i] * count         # Subtract the value
            
        return roman
    
    
    
sol = Solution()
print(sol.intToRoman(1994))  # Output: MCMXCIV
print(sol.intToRoman(58))    # Output: LVIII
print(sol.intToRoman(9))     # Output: IX


