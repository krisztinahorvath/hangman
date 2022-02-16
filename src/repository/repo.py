class Repository:
    def __init__(self, file_name):
        self._file_name = file_name
        self._sentence_list = list()
        self._load_file()

    def _load_file(self):
        """
        Load text file and read the sentences from it.
        :return:
        """
        f = open(self._file_name, "rt")
        for line in f.readlines():
            line = line.strip()
            if len(line) > 0:
                self._sentence_list.append(line)

        self._save_file()
        f.close()

    def _save_file(self):
        """
        Saves file, writes everything in the file and saves it.
        :return:
        """
        f = open(self._file_name, "wt")
        for i in self._sentence_list:
            f.write(str(i) + '\n')

        f.close()

    def add_sentence(self, sentence):
        """
        Adds a sentence to the sentence list and saves it to the file.
        :return:
        """
        self._sentence_list.append(sentence)
        self._save_file()

    @property
    def sentence_list(self):
        return self._sentence_list






