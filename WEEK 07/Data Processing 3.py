def longest_antakshari_subsequence(seq):
    words = seq.split(",")
    max_len = 1
    curr_len = 1

    for i in range(1, len(words)):
        if words[i - 1][-1] == words[i][0]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1  # reset the length

    return max_len


# Read input
n = int(input())
for _ in range(n):
    line = input().strip()
    print(longest_antakshari_subsequence(line))
