from dataclasses import dataclass

type freq = float
type proba = float

@dataclass
class Token:
    word: str
    frequency: freq
    next_words: dict[int, list[freq | proba]]

class MarkovChainAnalyser:
    dictionnary: list[Token]

    def __init__(self) -> None:
        self.dictionnary = []

    def idx_of_word_in_dict(self, searched_word: str) -> int:
        """returns -1 if it is not found"""
        for i, word in enumerate(self.dictionnary):
            if word.word == searched_word:
                return i
            
        return -1

    def analyse_text(self, text: str):
        words = text.lower().replace(",", " , ").replace(".", " . ").replace("!", " ! ").replace("?", " ? ").split()

        for word, next_word in zip(words, words[1::]):
            if (i := self.idx_of_word_in_dict(word)) == -1:
                i = len(self.dictionnary)
                self.dictionnary.append(Token(word, 0, {}))

            self.dictionnary[i].frequency += 1
            print(self.dictionnary[i].frequency, i)
            next_idx = self.idx_of_word_in_dict(next_word)
            if next_idx == -1:
                next_idx = len(self.dictionnary)
                self.dictionnary.append(Token(next_word, 0, {}))

            print(self.dictionnary[i].frequency, i)
            if self.dictionnary[i].next_words.get(next_idx) is None:
                self.dictionnary[i].next_words[next_idx] = [ 0, 0 ]

            self.dictionnary[i].next_words[next_idx][0] += 1
            self.dictionnary[i].next_words[next_idx][1] = self.dictionnary[i].next_words[next_idx][0] / self.dictionnary[i].frequency

            

        print(self.dictionnary)
def main():
    makov_analyser = MarkovChainAnalyser()
    makov_analyser.analyse_text("hello, world !")

if __name__ == "__main__":
    main()