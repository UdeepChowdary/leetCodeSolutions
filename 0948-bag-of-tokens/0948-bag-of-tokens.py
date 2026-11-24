class Solution:
    def bagOfTokensScore(nlnself, tokens: list[int], power: intn) -> int:
        tokens.sort()
        
        max_score = 0
        current_score = 0
        left = 0
        right = len(tokens) - 1
        
        while left <= right:
            if power >= tokens[left]:
                power = power - tokens[left]
                current_score = current_score + 1
                left = left + 1
                if current_score > max_score:
                    max_score = current_score
            elif current_score >= 1:
                power = power + tokens[right]
                current_score = current_score - 1
                right = right - 1
            else:
                break
                
        return max_score