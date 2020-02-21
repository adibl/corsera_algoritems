class FindPattern(object):
    PRIME = 1073676287
    X = random.randrange(1, 1073676287 - 1)
    M = 10 ** 4

    def PolyHashFunction(cls):
        return lambda string: sum([ord(string[i]) * (cls.X ** i) for i in range(len(string))]) % cls.PRIME

    def __init__(self, string):
        self.text = string

    def get_matches(self, pattern):
        results = []
        hash_function = self.PolyHashFunction()
        index_start = len(self.text) - len(pattern)
        index_end = len(self.text)
        string_hash = hash_function(self.text[index_start: index_end])
        pattern_hash = hash_function(pattern)
        if string_hash == pattern_hash:
            results.append(index_start)
        removal_number = 1
        for i in range(1, len(pattern)):
            removal_number = (removal_number * self.X) % self.PRIME
        for index in range(index_start - 1, -1, -1):
            adition = ord(self.text[index]) - (removal_number * self.X * ord(self.text[index + len(pattern)]))
            string_hash = (string_hash * self.X + adition) % self.PRIME
            if string_hash == pattern_hash:
                if self.text[index: index + len(pattern)] == pattern:
                    print(index) + ' '


str1 = input()
str2 = input()
FindPattern(str2).get_matches(str1)
