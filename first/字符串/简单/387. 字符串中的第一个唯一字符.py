class Num387(object):
    @staticmethod
    def leetcode(s):
        res = len(s)
        for i in set(s):
            if s.count(i) == 1 and s.index(i) < res:
                res = s.index(i)
        if res == len(s):
            return -1
        return res


def main():
    tmp = Num387.leetcode("a")
    print(tmp)


if __name__ == '__main__':
    main()
