from typing import List, Dict


class Solution:
    def check_minimal_length(self,
                             nums: List[int],
                             MINIMAL_LENGTH=2) -> tuple[bool, List[int]]:
        if len(nums) == MINIMAL_LENGTH:
            return True, [value for value in range(MINIMAL_LENGTH)]
        return False, []

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # d = {}
        # for i, j in enumerate(nums):
        #     r = target - j
        #     if r in d:
        #         return [d[r], i]
        #     d[j] = i

        answer: List[int] = []
        current: int = target

        if self.check_minimal_length(nums)[0]:
            return self.check_minimal_length(nums)[1]

        for value in nums:
            current = target - value
            if target == 0:
                answer.append(nums.index(value))
                nums[nums.index(value)] = None
                answer.append(nums.index(current))
                return answer
            answer.append(nums.index(value))
            nums[nums.index(value)] = None
            if current in nums:
                answer.append(nums.index(current))
                return answer
            answer.pop()
        return answer

    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False

    def isPalindrome_v2(self, x: int) -> bool:
        if x < 0:
            return False
        reverse_number = 0
        original_number = x

        while x != 0:
            print(x % 10)
            reverse_number = reverse_number * 10 + x % 10
            x //= 10
        return reverse_number == original_number

    def romanToInt(self, s: str) -> int:
        roman_to_decimal: Dict[str, int] = {
            'I': 1, 'IV': 4, 'V': 5, 'VI': 6, 'IX': 9, 'X': 10, 'XX': 20,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
            'DC': 600, 'CM': 900, 'M': 1000,
        }

        temp_result: List[int] = []
        result: List[int] = []

        for index, value in enumerate(s):
            if value in ['I']:
                if index + 1 < len(s) and s[index + 1] in ['V', 'X']:
                    temp_result.append(value + s[index + 1])
                    result.append(
                        roman_to_decimal.get(value + s[index + 1], 0))
                    continue
            if value in ['X']:
                if index + 1 < len(s) and s[index + 1] in ['L', 'C']:
                    temp_result.append(value + s[index + 1])
                    result.append(
                        roman_to_decimal.get(value + s[index + 1], 0))
                    continue
            if value in ['C']:
                if index + 1 < len(s) and s[index + 1] in ['D', 'M']:
                    temp_result.append(value + s[index + 1])
                    result.append(
                        roman_to_decimal.get(value + s[index + 1], 0))
                    continue
            if value in roman_to_decimal:
                temp_result.append(value)
                result.append(roman_to_decimal.get(value, 0))
                if index - 1 >= 0 and len(temp_result[index - 1]) == 2:
                    result.pop()
        return sum(result)

    def roman_to_int_v2(self, s: str) -> int:
        roman_to_decimal: Dict[str, int] = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result: int = 0

        for index, value in enumerate(s):
            if index + 1 < len(s) and (roman_to_decimal.get(value)
                                       < roman_to_decimal.get(s[index + 1])):
                result -= roman_to_decimal.get(value)
            else:
                result += roman_to_decimal.get(value)
        return result

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: str = ''
        strs.sort(key=len)
        if len(strs) in [0, 1]:
            return strs[0]

        for index, letter in enumerate(strs[0]):
            prefix += letter
            for value in strs:
                if not value.startswith(prefix):
                    return prefix[:-1]
        return prefix

    def lastStoneWeight(self, stones: List[int]) -> int:

        def brake_stones(a: int, b: int) -> int:
            if a == b:
                return 0
            return b - a

        stones.sort()
        temp: int = 0
        for _ in range(len(stones)):
            if len(stones) >= 2:
                temp = brake_stones(stones[-2], stones[-1])
                stones.pop()
                stones.pop()
                stones.append(temp)
                stones.sort()
        return stones[0]


s1 = Solution()

assert s1.twoSum([2, 7, 11, 17], 9) == [0, 1]
assert s1.twoSum([3, 2, 4], 6) == [1, 2]
assert s1.twoSum([0, 4, 3, 0], 0) == [0, 3]
assert s1.twoSum([3, 3], 6) == [0, 1]
assert s1.twoSum([3, 2, 3], 6) == [0, 2]
assert s1.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

assert s1.roman_to_int_v2('III') == 3
assert s1.roman_to_int_v2('LVIII') == 58
assert s1.roman_to_int_v2('MCMXCVI') == 1996

assert s1.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
assert s1.longestCommonPrefix(["ab", "a"]) == 'a'

assert s1.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
