class Num819(object):
    @staticmethod
    def leetcode(paragraph, banned):
        word_num = {}
        para_list = paragraph.lower().split(' ')
        for i, j in enumerate(para_list):
            if not j.isalpha():
                j = j[:-1]
            if j not in word_num.keys():
                word_num[j] = 1
                continue
            word_num[j] += 1
        for i in range(len(word_num)):
            max_word = max(word_num, key=word_num.get)
            if max_word in banned:
                word_num[max_word] = 0
                continue
            return max_word


def main():
    tmp = Num819.leetcode("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(tmp)


if __name__ == '__main__':
    main()
