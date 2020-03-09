class Num49(object):
    @staticmethod
    def leetcode(strs):
        dic = {}
        for i in strs:
            ls = [ord(x) for x in i]
            ls.sort()
            asc = tuple(ls)
            if asc not in dic.keys():
                dic[asc] = [i,]
                continue
            dic[asc].append(i)
        return [x for x in dic.values()]



def main():
    tmp = Num49.leetcode(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(tmp)


if __name__ == '__main__':
    main()
