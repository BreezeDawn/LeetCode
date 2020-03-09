class Num859(object):
    @staticmethod
    def leetcode(A, B):
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(A)) >= len(A):
                return False
            return True
        sign = 0
        m = None
        n = None
        for i, j in enumerate(A):
            if j != B[i]:
                if m:
                    if sign:
                        return False
                    if j != n or B[i] != m:
                        return False
                    sign = 1
                    continue
                m = j
                n = B[i]
        else:
            if not sign:
                return False
            return True


def main():
    tmp = Num859.leetcode("ab", "ab")
    print(tmp)


if __name__ == '__main__':
    main()
