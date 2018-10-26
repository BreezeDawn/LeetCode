class Num788(object):
    @staticmethod
    def leetcode(N):
        dic = ['0', '1', '2', '5', '6', '8', '9']
        res = 0
        for i in range(N + 1):
            i = str(i)
            for j in i:
                if j not in dic:
                    break
            else:
                if ('2' in i) or ('5' in i) or ('6' in i) or ('9' in i):
                    res += 1
        return res


def main():
    tmp = Num788.leetcode(16)
    print(tmp)


if __name__ == '__main__':
    main()
