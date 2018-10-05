import bisect


def min_dec_subsequence(nums):
    """Given a list of numbers, return the minimum number of strictly decreasing sub-sequences.
    In a real world scenario, given a list of children in a line, assign the children from the head of the line to
    different queues such that each queue goes from tallest to shortest and the number of queues is minimum.
    """
    num_subseq = 0
    subseq_ends = []  # the heights of those children at the end of each queue, in sorted order
    for num in nums:
        pos = bisect.bisect(subseq_ends, num)
        if pos == len(subseq_ends):
            num_subseq += 1
            subseq_ends.insert(pos, num)
        else:
            subseq_ends[pos] = num
    return num_subseq


def min_dec_sseq_test():
    inputs = [[5, 4, 3, 6, 1], [5, 4, 8, 9, 9, 4, 3, 7, 2, 1, 5, 3, 7]]
    outputs = [2, 4]
    for i in range(len(inputs)):
        assert min_dec_subsequence(inputs[i]) == outputs[i], "failed test %i" % i
    return "all tests pass"

if __name__ == "__main__":
    print(min_dec_sseq_test())
