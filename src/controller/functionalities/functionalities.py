from random import choice
from src.repository.repo import Repository
from copy import deepcopy
from src.controller.functionalities.validations import ValidationError, Validations


class Controller:
    def __init__(self, file_name):
        self.repo = Repository(file_name)
        self.sentence_solution = self.random_sentence()
        self.sentence_in_game = self.codify_sentence()
        self.hangman = ""

    def random_sentence(self):
        return choice(self.repo.sentence_list)

    def add_sentence(self, sentence):
        try:
            sentence = sentence.strip()
            valid = Validations(sentence, self.repo.sentence_list)
            valid.valid_sentence()
            self.repo.add_sentence(sentence)
        except ValidationError as ve:
            raise ve
        except IOError as ve:
            raise ve

    def codify_sentence(self):
        """
        pick the last and first letters of every sentence in a list, go through the sentence again
        and make all those letters underscores
        :return:
        """
        new_sentence = ""
        sent = deepcopy(self.sentence_solution)
        letters_to_be_shown = ""
        for word in sent.split(" "):
            letters_to_be_shown = letters_to_be_shown + word[0] + word[-1]
        for word in sent.split(" "):
            new_sentence = new_sentence + word[0]
            for i in range(1, len(word)-1):
                if word[i] in letters_to_be_shown:
                    new_sentence = new_sentence + word[i]
                else:
                    new_sentence = new_sentence + '_'
            new_sentence = new_sentence + word[-1] + ' '

        new_sentence = new_sentence.strip()
        return new_sentence

    def game_won_human(self):
        pass

    def game_won_computer(self):
        pass

    def wrong_letter(self):
        pass

    def right_letter(self):
        pass

    def letter_check(self):
        """
        uses wrong letter and right letter and game won human/computer
        :return:
        """
        pass
