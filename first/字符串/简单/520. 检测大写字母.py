class Num520(object):
    @staticmethod
    def leetcode(word):
        return word.isupper() or word.islower() or word[1:].islower()  # 最后这个应该使用 word.istitle()是否是单词首字母大写


def main():
    tmp = Num520.leetcode("Waw")
    print(tmp)


if __name__ == '__main__':
    main()
