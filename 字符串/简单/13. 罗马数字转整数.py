class Num13(object):
    @staticmethod
    def leetcode(s):
        res = 0
        special_list = [['IV', 4], ['IX', 9], ['XL', 40], ['XC', 90], ['CD', 400], ['CM', 900],
                        ['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]
        for i in special_list:
            res = res + s.count(i[0]) * i[1]
            s = s.replace(i[0], '')
        return res


def main():
    tmp = Num13.leetcode('MCMXCIV')
    print(tmp)


if __name__ == '__main__':
    main()
