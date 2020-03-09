class Num217(object):
    @staticmethod
    def select(nums):
        if not nums:
            return False
        nums.sort()
        n = 0
        list_len = len(nums) - 1
        while n < list_len:
            if nums[n] == nums[n + 1]:
                return True
            else:
                n = n + 1
        return False


def main():
    tmp = Num217.select([1, 2, 3, 1])
    print(tmp)


if __name__ == '__main__':
    main()
