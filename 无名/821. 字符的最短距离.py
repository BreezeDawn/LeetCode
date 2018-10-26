class Num821(object):
    @staticmethod
    def leetcode(S, C):
        res = []
        prior = None
        index = 0
        real_index = 0
        for i in S[:]:
            real_index += 1
            if i != C:
                index += 1
                if real_index == len(S):
                    m = 0
                    for x in range(index):
                        m += 1
                        res.append(m)
                continue
            if not prior:
                for x in range(index + 1, 0, -1):
                    res.append(i - 1)
                index = 0
                prior = 1
                continue
            if prior:
                if index % 2:
                    index += 1
                    num = 0
                    for x in range(index // 2):
                        num += 1
                        res.append(num)
                    for y in range(index // 2):
                        num -= 1
                        res.append(num)
                    index = 0
                else:
                    num = 0
                    for x in range(index // 2):
                        num += 1
                        res.append(num)
                    for y in range(index // 2):
                        res.append(num)
                        num -= 1
                    res.append(0)
                    index = 0
        return res


def main():
    tmp = Num821.leetcode(S="qingfengliangchen", C='n')
    print(tmp)


if __name__ == '__main__':
    main()
