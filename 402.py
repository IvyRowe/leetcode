def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if not num or k == len(num):
        return '0'
    result = []
    for n in num:
        while result and result[-1] > n and k > 0:
            result.pop()
            k-=1
        result.append(n)
    if k > 0:
        result[:] = result[:-k]
    if not result:
        return '0'
    return str(int(''.join(result)))

def main():
    num = '1234567890'
    x = removeKdigits(num, 9)
    print x

if __name__ == "__main__": main()
