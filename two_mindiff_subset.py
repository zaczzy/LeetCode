import time
def two_mindiff_subset(nums):
    sum_total = sum(nums)
    sum_half = sum_total // 2
    l = len(nums)
    achievable = [[False for _ in range(l + 1)] for _ in range(sum_half)]
    achievable.insert(0, [True for _ in range(l + 1)])
    for i in range(1, sum_half + 1):
        for j in range(1, l + 1):
            if achievable[i][j - 1] or i - nums[j - 1] >= 0 and achievable[i - nums[j - 1]][j - 1]:
                achievable[i][j] = True
    achievable_sums = [any(row) for row in achievable]

    k = sum_half
    while k >= 0:
        if achievable_sums[k]:
            break
        k -= 1
    return sum_total - k * 2


def min_diff_subset_test():
    inputs = [[1, 7], [2, 3, 4, 5], [1, 2, 3, 4, 5, 30]]
    outputs = [6, 0, 15]
    for i in range(len(inputs)):
        t = time.time()
        assert two_mindiff_subset(inputs[i]) == outputs[i], "failed test %i, should get %i, but got %i" % (i, outputs[
            i], two_mindiff_subset(inputs[i]))
        print(time.time() - t)
    return "all tests pass"


if __name__ == "__main__":
    print(min_diff_subset_test())
