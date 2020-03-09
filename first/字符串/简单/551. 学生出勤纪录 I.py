class Num551(object):
    @staticmethod
    def leetcode(s):
        return (s.count('A') < 2) and ('LLL' not in s)


def main():
    tmp = Num551.leetcode("PPAALL")
    print(tmp)


if __name__ == '__main__':
    main()
