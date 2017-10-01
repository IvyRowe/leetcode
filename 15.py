def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: # check for duplicated and care i=0
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l+=1
            elif s > 0:
                r-=1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l+=1
                while l < r and nums[r] == nums[r-1]:
                    r-=1
                l+=1; r-=1
    return result

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    x = threeSum(nums)
    print x

if __name__ == "__main__": main()
