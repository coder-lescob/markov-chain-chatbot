from dataclasses import dataclass

type freq = float
type proba = float

@dataclass
class Token:
    word: str
    frequency: freq
    next_words: dict[int, list[freq | proba]]

    @staticmethod
    def from_dict(dictionnary):
        return Token(dictionnary["word"], dictionnary["frequency"], dictionnary["next_words"])