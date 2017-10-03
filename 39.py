def help(target, result, index, path, nums):
    if target < 0:
        return
    if target == 0:
        result.append(path)
    for i in xrange(index, len(nums)):
        help(target-nums[i], result, i, path+[nums[i]], nums)

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []
    candidates.sort()
    help(target, result, 0, [], candidates)
    return result

def main():
    nums = [2, 3, 6, 7]
    target = 7
    x = combinationSum(nums, target)
    print x

if __name__ == "__main__": main()
