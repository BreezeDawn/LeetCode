class Num686(object):
    @staticmethod
    def leetcode(A, B):
        count = 1
        a = A
        while len(a) <= 10000:
            if B in a:
                return count
            count += 1
            a += A
        return -1


def main():
    tmp = Num686.leetcode("abcd", "cdabcdab")
    print(tmp)


if __name__ == '__main__':
    main()
