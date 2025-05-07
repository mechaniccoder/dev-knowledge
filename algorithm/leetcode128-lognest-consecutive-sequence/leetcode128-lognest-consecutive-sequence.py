from typing import List


# Hash Set: numsㅇ서의 중복제거, 검색 시간복잡도가 O(1)이기 때문에 효율적으로 sequence를 찾을 수 있다.
# Union & Find: sequence가 시작되는 root를 찾는게 핵심이다. nums - 1가 Hash Set에 존재하면 root가 아니므로 pass하고,
# 존재하지 않다면 root이므로 해당 숫자부터 시작하여 sequence 길이를 계산한다.
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if (num - 1) not in numsSet:
                length = 0

                while num + length in numsSet:
                    length += 1

                longest = max(longest, length)

        return longest
