class Num516(object):
    @staticmethod
    def leetcode(nums):
        nums.sort()
        return sum(nums[::2])


def main():
    tmp = Num516.leetcode([1, 4, 4, 9, 3, 2])
    print(tmp)


if __name__ == '__main__':
    main()
