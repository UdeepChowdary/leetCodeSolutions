## time comp - O(2^n*L), space comp - O(2^n*L)
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        valid_combinations = [""]
        max_length = 0

        for word in arr:
            if len(set(word)) != len(word):
                continue

            new_combinations = []
            for existing in valid_combinations:
                combined = existing + word
                if len(set(combined)) == len(combined):
                    new_combinations.append(combined)
                    if len(combined) > max_length:
                        max_length = len(combined)

            valid_combinations.extend(new_combinations)

        return max_length