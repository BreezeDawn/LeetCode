class Num434(object):
    @staticmethod
    def leetcode(s):
        return len(s.split())


def main():
    tmp = Num434.leetcode(
        "The one-hour drama series Westworld is a dark odyssey about the dawn of artificial"
        " consciousness and the evolution of sin. Set at the intersection of the near future "
        "and the reimagined past, it explores a world in which every human appetite, no matter "
        "how noble or depraved, can be indulged.")
    print(tmp)


if __name__ == '__main__':
    main()
