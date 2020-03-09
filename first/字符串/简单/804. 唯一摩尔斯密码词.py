class Num804(object):
    @staticmethod
    def leetcode(words: list) -> int:
        base_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                     "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                     "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                     "y": "-.--", "z": "--.."}

        tmp_result = []
        for word in words:
            tmp_word = ""
            for s in word:
                tmp_word += base_dict[s]
            else:
                if tmp_word not in tmp_result:
                    tmp_result.append(tmp_word)

        return len(tmp_result)


def main():
    tmp = Num804.leetcode(["gin", "zen", "gig", "msg"])
    print(tmp)


if __name__ == '__main__':
    main()
