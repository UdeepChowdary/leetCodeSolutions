## time comp - O(4^n*n), space comp - O(4^n*n)
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = [""]

        for digit in digits:
            letters = digit_to_letters[digit]
            next_combinations = []

            for prefix in combinations:
                for letter in letters:
                    next_combinations.append(prefix + letter)

            combinations = next_combinations

        return combinations