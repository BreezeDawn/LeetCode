class Num657(object):
    @staticmethod
    def leetcode(moves):
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')


def main():
    tmp = Num657.leetcode("UD")
    print(tmp)


if __name__ == '__main__':
    main()
