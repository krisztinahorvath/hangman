"""
Repository class that contains the sentence list and the functions for opening, saving a file plus others
needed to play the game or to save a sentence.
"""


class Repository:
    def __init__(self, file_name):
        self._file_name = file_name
        self._sentence_list = list()
        self.load_file()

    def load_file(self):
        """
        Load text file and read the sentences from it.
        :return:
        """
        try:
            f = open(self._file_name, "rt")
            for line in f.readlines():
                line = line.strip()
                if len(line) > 0:
                    self._sentence_list.append(line)

            self.save_file()
            f.close()
        except IOError as ve:
            raise ve

    def save_file(self):
        """
        Saves file, writes everything in the file and saves it.
        :return:
        """
        try:
            f = open(self._file_name, "wt")
            for i in self._sentence_list:
                f.write(str(i) + '\n')

            f.close()
        except IOError as ve:
            raise ve

    def add_sentence(self, sentence):
        """
        Adds a sentence to the sentence list and saves it to the file.
        :param sentence: sentence given by user
        :return:
        """
        self._sentence_list.append(sentence)
        self.save_file()

    @property
    def sentence_list(self):
        return self._sentence_list






