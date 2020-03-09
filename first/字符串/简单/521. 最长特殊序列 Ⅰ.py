class Num521(object):
    def leetcode(self, a, b):
        # 这是脑筋急转弯吧!
        if a == b:
            return -1
        else:
            return max(len(a), len(b))


def main():
    tmp = Num521.leetcode("aba", "cdc")
    print(tmp)


if __name__ == '__main__':
    main()
