class Num553(object):
    @staticmethod
    def leetcode(nums):
        if len(nums) == 2:
            return repr(nums)[1:-1].replace(',', '/').replace(' ', '')
        res_top = nums.pop(0)
        if not nums:
            return repr(res_top)
        return repr(res_top) + '/(' + repr(nums)[1:-1].replace(',', '/').replace(' ', '') + ')'


def main():
    tmp = Num553.leetcode([2, 3])
    print(tmp)


if __name__ == '__main__':
    main()
