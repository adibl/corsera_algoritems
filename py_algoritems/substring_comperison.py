import random


class FindPattern(object):
    X = random.randrange(1, 10 ** 9)
    M1 = 10 ** 9 + 7
    M2 = 10 ** 9 + 9

    def __init__(self, string):
        self.text = string
        self.hashes = [0] 
        self.hashes2 = [0]
        for i in range(1, len(self.text) + 1):
            self.hashes.append((self.hashes[i - 1] * self.X + ord(self.text[i - 1])) % self.M1)
            self.hashes2.append((self.hashes2[i - 1] * self.X + ord(self.text[i - 1])) % self.M2)

    def is_equal_substrings(self, start1, start2, length):
        x_mod1 = pow(self.X, length, self.M1)
        hash1_1 = (self.hashes[start1 + length] - self.hashes[start1] * x_mod1) % self.M1
        hash2_1 = (self.hashes[start2 + length] - self.hashes[start2] * x_mod1) % self.M1
        if hash1_1 == hash2_1:
            x_mod2 = pow(self.X, length, self.M2)
            hash1_2 = (self.hashes2[start1 + length] - self.hashes2[start1] * x_mod2) % self.M2
            hash2_2 = (self.hashes2[start2 + length] - self.hashes2[start2] * x_mod2) % self.M2
            if hash2_2 == hash1_2:
                return True
        return False


def test_substring_hash():
    f = FindPattern('123412')
    assert f.is_equal_substrings(0, 4, 2) is True


def test_from_pdf():
    f = FindPattern('trololo')
    assert f.is_equal_substrings(0, 0, 7) is True
    assert f.is_equal_substrings(2, 4, 3) is True
    assert f.is_equal_substrings(3, 5, 1) is True
    assert f.is_equal_substrings(1, 3, 2) is False
