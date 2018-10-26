class Num1(object):
    @staticmethod
    def twosum(nums, target):
        sli = nums[:]
        for i in nums:
            sli.remove(i)
            if target - i in sli:
                n = nums.index(i)
                nums[n] = i + 1
                m = nums.index(target - i)
                return n, m


def main():
    tmp = Num1.twosum([7, 2, 2, 15], 4)
    print(tmp)


if __name__ == '__main__':
    main()
