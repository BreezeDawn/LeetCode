class Num38(object):
    @staticmethod
    def leetcode(n):
        if n == 1:
            return '1'
        last = '1'
        tmp = ''
        while n > 1:
            num = 1
            for i, j in enumerate(last):
                if i + 1 <= len(last) - 1:
                    if j == last[i + 1]:
                        num += 1
                        continue
                tmp = tmp + str(num) + j
                num = 1
            n -= 1
            last = tmp
            tmp = ''
        return last


def main():
    tmp = Num38.leetcode(5)
    print(tmp)


if __name__ == '__main__':
    main()
