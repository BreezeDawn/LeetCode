class Num647(object):
    @staticmethod
    def leetcode(s):
        res = 0
        length = len(s)
        for i, j in enumerate(s):
            k = i
            while k < length:
                if s[i:k + 1] == s[i:k + 1][::-1]:
                    res += 1
                k += 1
        return res


def main():
    tmp = Num647.leetcode("aaa")
    print(tmp)


if __name__ == '__main__':
    main()
