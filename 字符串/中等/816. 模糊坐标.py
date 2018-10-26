class Num816(object):
    @staticmethod
    def leetcode(S):
        S = S[1:-1]
        ans = []
        res = []
        for i in range(len(S) - 1):
            tmp = []
            tmp.append(S[:i + 1])
            tmp.append(S[i + 1:])
            ans.append(tmp)
        for i in ans:
            for m in range(len(i[0])):
                if len(i[0]) != 1 and m != len(i[0]) - 1:
                    s1 = i[0][:m + 1] + '.' + i[0][m + 1:]
                else:
                    s1 = i[0]
                if (s1.startswith('0') and s1.endswith('0') and len(s1) != 1) or (s1.startswith('00')) \
                        or ('.' in s1 and s1.endswith('0')) or (
                        s1.startswith('0') and not s1.startswith('0.') and len(s1) != 1):
                    continue
                for n in range(len(i[1])):
                    if len(i[1]) != 1 and n != len(i[1]) - 1:
                        s2 = i[1][:n + 1] + '.' + i[1][n + 1:]
                    else:
                        s2 = i[1]
                    if (s2.startswith('0') and s2.endswith('0') and len(s2) != 1) or (s2.startswith('00')) \
                            or ('.' in s2 and s2.endswith('0')) or (
                            s2.startswith('0') and not s2.startswith('0.') and len(s2) != 1):
                        continue
                    res.append((s1, s2))
        return ['({}, {})'.format(*e) for e in res]


def main():
    tmp = Num816.leetcode("(0000001)")
    print(tmp)


if __name__ == '__main__':
    main()
