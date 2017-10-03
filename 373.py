def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    if len(nums1)*len(nums2) < k:
        return [[m, n] for m in nums1 for n in nums2]
    hp = [[n + nums2[0], n, 0] for n in nums1]
    res = []
    for i in range(k):
        psum, n, ind = hp[0]
        res.append([n, psum-n])
        if ind + 1 == len(nums2):
            heapq.heappop(hp)
        else:
            heapq.heapreplace(hp, [n, nums[ind+1], n, ind+1])
    return res

def main():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 2
    x = kSmallestPairs(nums1, nums2, k)
    print x

if __name__ == "__main__": main()
