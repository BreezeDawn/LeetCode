class Num14(object):
    @staticmethod
    def leetcode(strs):
        if not strs:
            return ''
        num = 0
        for i in range(len(strs[0]) + 1):
            s = strs[0][0:num]
            for j in strs:
                if j.startswith(s):
                    continue
                return strs[0][0:num - 1]
            num += 1
        else:
            return s


def main():
    tmp = Num14.leetcode(["flower", "flowerr", "flight"])
    print(tmp)
    tmp2 = Num14.leetcode(["flower", "dlow", "clight"])
    print(tmp2)
    tmp3 = Num14.leetcode(['a'])
    print(tmp3)


if __name__ == '__main__':
    main()
