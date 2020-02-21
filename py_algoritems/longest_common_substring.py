import math
import random


class LongestCommon(object):
    X = random.randrange(1, 10 ** 9)
    M1 = 10 ** 9 + 7
    M2 = 10 ** 9 + 9

    @classmethod
    def PolyHashFunction(cls, string, m):
        return sum([ord(string[i]) * (cls.X ** i) for i in range(len(string))]) % m

    def __init__(self, string, string2):
        self.string1 = string
        self.string2 = string2
        self.hashes = [0]
        self.hashes2 = [0]
        for i in range(1, len(self.string1) + 1):
            self.hashes.append((self.hashes[i - 1] * self.X + ord(self.string1[i - 1])) % self.M1)
        for i in range(1, len(self.string2) + 1):
            self.hashes2.append((self.hashes2[i - 1] * self.X +
                                ord(self.string2[i - 1])) % self.M1)

    def result(self):
        """
        the running time of is_eudql_substring is O(len(sting1) + len(string2) - length)
        thus to divide {1,2,3,4.....totoal_len} to 2 parts with equal sum
        miidle_sum = 1.5 of the middle of the string
        {1...v/2|v/2+1 ... v} so the difference betwwn the 2 sides is number of vlaues (v/2) multiplied by different per value (v/2)
        thus we need to move numbers equal to v^2/4 to the first group.
        every var in the secend grotp is larger then v/2 so 2 is a good choise
        then there will be v/2 * v/4 more nubbers in the first group, which mesan movig v^2/8 form one group to another
        """
        max_length = 0
        indexes = (0, 0)
        mid_len = min(len(self.string1) , len(self.string2)) 
        middle_number = mid_len + mid_len // 2 
        while 0 < middle_number <= min(len(self.string1), len(self.string2)) and middle_number > max_length:
            data = self.is_euql_substrings(middle_number)
            if data is not None:
                max_length = middle_number
                indexes = data
                substring_len = mid_len - middle_number
                middle_number = middle_number + substring_len // 2
            else:
                substring_len = middle_number
                middle_number = middle_number - substring_len // 2
        return indexes + (max_length, )

    def is_euql_substrings(self, length):
        dictionary = {}
        for i in range(0, len(self.string1) - length + 1):
            hashed = self.compute_hash(i, length, self.M1, self.hashes)
            if hashed in dictionary:
                dictionary[hashed].append(i)
            else:
                dictionary[hashed] = [i]
        for i in range(0, len(self.string2) - length + 1):
            hashed_value = self.compute_hash(i, length, self.M1, self.hashes2)
            data = dictionary.get(hashed_value)
            if data is not None:
                hash_1 = self.PolyHashFunction(self.string1[data[0]:data[0] + length], self.M2)
                hash_2 = self.PolyHashFunction(self.string2[i: i + length], self.M2)
                if hash_1 == hash_2:
                    return data[0], i
        return None

    def compute_hash(self, start, length, m, hashes):
        x_mod = pow(self.X, length, m)
        partial_hash = (hashes[start + length] - hashes[start] * x_mod) % m
        return partial_hash


def test_is_equal_substring():
    l = LongestCommon('cool', 'toolbox')
    assert l.is_euql_substrings(3) == (1, 1)


def test_is_equal_substring2():
    l = LongestCommon('aabaa',  'babbaab')
    assert l.is_euql_substrings(3) == (2, 3)


def test_is_equal_substring_no_match():
    l = LongestCommon('aaaaaa', 'bbbbb')
    for i in range(1, 5):
        assert l.is_euql_substrings(i) is None


def test_from_pdf():
    l = LongestCommon('cool', 'toolbox')
    assert l.result() == (1, 1, 3)
    l = LongestCommon('aaa', 'bb')
    assert l.result() == (0, 0, 0)
    l = LongestCommon('aabaa', 'babbaab')
    assert l.result() == (2, 3, 3)


def test_edges():
    l = LongestCommon('ab', 'asdfab')
    assert l.result() == (0, 4, 2)
    l = LongestCommon('ab',  'asdfab')
    assert l.result() == (0, 4, 2)
