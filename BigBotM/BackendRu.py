import requests
from Definition import search_word_definition


class Grammar:
    def __init__(self, word: str, letters_to_check: list):
        self.word = word
        self.letters_to_check = letters_to_check
        self.number = 0

    def check_for_existence(self, _word) -> bool:
        _word += "\n"
        with open('text.txt', 'r', encoding="utf-8") as ru:
            a = ru.readlines()
            if _word in a:
                return True
            else:
                return False

    def replacement(self, _word: list, value) -> str:
        n = 0
        wordList_word = _word.copy()
        for i in wordList_word:
            if i == "_":
                wordList_word.remove("_")
                wordList_word.insert(n, value)
                self.number = n
                return "".join(wordList_word)

            n += 1
        return "underscore not found"

    def highlighting_word(self, _word) -> str:
        _wordList = list(_word)
        _wordList[self.number] = _wordList[self.number].upper()
        return "".join(_wordList)

    def find_the_right_word(self):
        self.word = list(self.word)
        right_words = ""
        modifiedWord = ""
        for i in range(len(self.letters_to_check)):
            modifiedWord = self.replacement(self.word, self.letters_to_check[i])
            if self.check_for_existence(modifiedWord):
                right_words += (f"{search_word_definition(modifiedWord, 210)}\n \n")

        if right_words != "":
            return right_words

        return "Ошибка: Слово не распознано"


if __name__ == "__main__":

    a = Grammar('зал_ть', ['и','а','я','е','ы','о'])
    print(a.find_the_right_word())