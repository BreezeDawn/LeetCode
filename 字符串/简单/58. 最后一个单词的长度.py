class Num58(object):
    @staticmethod
    def leetcode(s):
        return len(s.rstrip().split(' ')[-1])


def main():
    tmp = Num58.leetcode("")
    print(tmp)


if __name__ == '__main__':
    main()
