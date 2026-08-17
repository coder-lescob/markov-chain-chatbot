from _token import Token
import json

class MarkovChainAnalyser:
    dictionnary: list[Token]
    previous_words: list[str]

    def __init__(self) -> None:
        self.dictionnary = []
        self.previous_words = []

    def idx_of_word_in_dict(self, searched_word: str) -> int:
        """returns -1 if it is not found"""
        for i, word in enumerate(self.dictionnary):
            if word.word[0] == searched_word:
                return i
            
        return -1

    def analyse_text(self, text: str):
        words = text \
            .lower() \
            .replace(",", " , ")\
            .replace(".", " . ")\
            .replace("!", " ! ")\
            .replace("?", " ? ")\
            .replace("'", "' ") \
            .replace("(", " ( ")\
            .replace(")", " ) ")\
            .split()
        words.insert(0, "")
        words.append("eof")

        for word, next_word in zip(words, words[1::]):
            if (i := self.idx_of_word_in_dict(word)) == -1:
                i = len(self.dictionnary)
                self.dictionnary.append(Token([word], 0, {}))

            self.dictionnary[i].frequency += 1
            next_idx = self.idx_of_word_in_dict(next_word)

            if next_idx == -1:
                next_idx = len(self.dictionnary)
                self.dictionnary.append(Token([next_word], 0, {}))

            if self.dictionnary[i].next_words.get(next_idx) is None:
                self.dictionnary[i].next_words[next_idx] = [ 0, 0 ]

            self.dictionnary[i].next_words[next_idx][0] += 1
            self.dictionnary[i].next_words[next_idx][1] = self.dictionnary[i].next_words[next_idx][0] / self.dictionnary[i].frequency

            self.previous_words.append(word)

    def toJson(self):
        return [
            {
                "word": token.word,
                "frequency": token.frequency,
                "next_words": token.next_words
            }

            for token in self.dictionnary
        ]

def main():
    makov_analyser = MarkovChainAnalyser()
    with open("training text.txt", "r") as file:
        makov_analyser.analyse_text(file.read())

    with open("output.json", "w") as file:
        file.write(json.dumps(makov_analyser.toJson(), indent=4))

if __name__ == "__main__":
    main()