class Num784(object):
    @staticmethod
    def leetcode(S):
        res_list = []
        letter_list = []
        letter_num = 0
        a = 0
        uplow = 0

        for i in S:
            if i.isalpha():
                letter_num += 1
                letter_list.append(i)

        res_list_num = 2 ** letter_num
        for i in range(res_list_num):
            res_list.append([])

        for i in S:
            if i in letter_list:
                num = 2 ** (letter_list.index(i) + 1)
                letter_list[letter_list.index(i)] = '1'
                n = len(res_list) // num
                while num:
                    for j in range(n):
                        if uplow:
                            res_list[a].append(i.upper())
                        else:
                            res_list[a].append(i.lower())
                        a += 1
                    if uplow:
                        uplow = 0
                    else:
                        uplow = 1
                    num -= 1
                a = 0
            else:
                for ls in res_list:
                    ls.append(i)
        res_res_list = []
        for i in res_list:
            res_res_list.append(''.join(i))
        return res_res_list


def main():
    Num784.leetcode("RmR")
    # tmp = Num784.leetcode("C3d4e5")


if __name__ == '__main__':
    main()
