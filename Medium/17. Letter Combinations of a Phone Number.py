class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(path, index):
            if len(path) == len(digits):
                result.append(path)
                return

            current_digit = digits[index]
            for letter in phone[current_digit]:
                backtrack(path + letter, index + 1)

        backtrack("", 0)
        return result

