import random
from model import word
from model import ball


class Main:
    word_list = []
    ball = ball.Ball()

    def __init__(self):
        pass

    def main(self):
        # take input (q for quit), build word list, shuffle list
        self.build_word_list()
        # get the first word, turn it into Word, cover it, print
        # repeatedly take input of index and letter
        for curr_word in self.word_list:
            curr_word = word.Word(curr_word)
            curr_word.cover_word()
            while curr_word.get_num_question() > 0:
                print(curr_word.covered_word)
                index, letter = self.get_response(curr_word)
                result = curr_word.check_index_correct(index, letter)
                self.check_after_response(curr_word, index, letter, result)
                if self.ball.is_fall():
                    print("sorry, the ball falls")
                    return
        print("congrats, you've finished your list!")

    def check_after_response(self, curr_word, index, letter, result):
        if result:
            curr_word.update_after_correct_answer(index, letter)
        else:
            self.ball.move_right()
            if not self.ball.is_fall():
                print(f"that is incorrect...the ball only has {self.ball.life} step(s) to fall :(")

    @staticmethod
    def get_response(curr_word):
        while True:
            try:
                index = int(input("Enter index: "))
                if curr_word.check_index_valid(index):
                    break
                else:
                    print("Please enter a valid index")
                    print(curr_word.covered_word)
            except ValueError:
                print("Please enter a valid index")
                print(curr_word.covered_word)
        letter = input("Enter letter: ")
        return index, letter

    def build_word_list(self):
        while True:
            user_input = input("Enter a word (q for finish entering): ")
            if user_input == "q" and len(self.word_list) < 1:
                print("need to have at least one word")
            elif user_input == "q":
                break
            if len(user_input) < 2:
                print("a word has to have a length larger than or equal to 2")
                continue
            self.word_list.append(user_input)
        random.shuffle(self.word_list)


main = Main()
if __name__ == '__main__':
    Main.main(main)
