class Num28(object):
    @staticmethod
    def leetcode(haystack, needle):
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


def main():
    tmp = Num28.leetcode("aaaaa", "bba")
    print(tmp)


if __name__ == '__main__':
    main()
