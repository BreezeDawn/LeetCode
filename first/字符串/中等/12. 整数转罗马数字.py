class Num12(object):
    @staticmethod
    def leetcode(num):
        res = ''
        dic = {0: ['V', 'I'], 1: ['L', 'X'], 2: ['D', 'C'], 3: ['M', 'M']}
        for i, j in enumerate(repr(num)[::-1]):
            if i < 3:
                if j == '9':
                    s = dic[i][1] + dic[i + 1][1]
                elif j == '4':
                    s = dic[i][1] + dic[i][0]
                else:
                    s = dic[i][0] * (eval(j) // 5) + dic[i][1] * (eval(j) % 5)
            else:
                s = eval(j) * dic[i][0]
            res = s + res
        return res


def main():
    tmp = Num12.leetcode(142)
    print(tmp)


if __name__ == '__main__':
    main()
