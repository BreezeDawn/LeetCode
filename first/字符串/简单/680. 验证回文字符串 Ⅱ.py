class Num680(object):
    @staticmethod
    def leetcode(s):
        k = 0
        s = list(s)
        s2 = s[::-1]
        for i, j in enumerate(s):
            if j == s2[k]:
                k += 1
                continue
            s.pop(i)
            if s == s[::-1]:
                return True
            s2.pop(i)
            if s2 == s2[::-1]:
                return True
            return False
        else:
            return True


def main():
    tmp = Num680.leetcode("cbbcc")
    print(tmp)


if __name__ == '__main__':
    main()
