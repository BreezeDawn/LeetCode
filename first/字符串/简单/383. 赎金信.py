class Num383(object):
    @staticmethod
    def leetcode(ransomNote, magazine):
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


def main():
    tmp = Num383.leetcode("aa", "ab")
    print(tmp)


if __name__ == '__main__':
    main()
