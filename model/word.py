import random as rd


class Word:
    word = ""
    covered_word = ""

    def __init__(self, input_word):
        self.word = input_word
        self.covered_word = input_word

    def cover_word(self):
        largest_index = len(self.word) - 1
        temp = list(self.covered_word)
        for i in range(largest_index):
            covered_index = rd.randint(0, largest_index)
            temp[covered_index] = "?"
        self.covered_word = "".join(temp)

    def check_index_valid(self, index) -> bool:
        if index < 0 or index > len(self.word) - 1 or self.covered_word[index] != "?":
            return False
        else:
            return True

    def check_index_correct(self, index, char) -> bool:
        return self.word[index] == char

