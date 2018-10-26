class Num67(object):
    @staticmethod
    def leetcode(a, b):
        return bin(eval('0b' + a) + eval('0b' + b))[2:]


def main():
    tmp = Num67.leetcode(a="11", b="1")
    print(tmp)


if __name__ == '__main__':
    main()
