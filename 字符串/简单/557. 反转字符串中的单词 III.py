class Num557(object):
    @staticmethod
    def leetcode(s):
        return ' '.join([x[::-1] for x in s.split(' ')])


def main():
    tmp = Num557.leetcode("Let's take LeetCode contest")
    print(tmp)


if __name__ == '__main__':
    main()
