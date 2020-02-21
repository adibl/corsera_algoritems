from longest_common_substring import LongestCommon
output = []
for _ in range(3):
    line = input().split()
    print(' '.join([str(x) for x in LongestCommon(line[0], line[1]).result()]))
