class Num541(object):
    @staticmethod
    def leetcode(s, k):
        count = len(s) // k
        res = ''
        sign = 2
        i = 0
        j = k
        while count:
            if sign % 2:
                res = res + s[i:j]
            else:
                res = res + s[i:j][::-1]
            i += k
            j += k
            count -= 1
            sign += 1
        if len(s) // k % 2:
            res = res + s[i:]
        else:
            res = res + s[i:][::-1]
        return res


def main():
    tmp = Num541.leetcode("abcdefg", 2)
    print(tmp)


if __name__ == '__main__':
    main()
