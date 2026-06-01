from _token import Token
import json
import random

class ChatBot:
    dictionnary: list[Token]

    def __init__(self) -> None:
        self.last_word = ""
        self.finish_generation = False

        with open("output.json", "r") as file:
            self.dictionnary = self.from_json(file.read())

    def idx_of_word_in_dict(self, searched_word: str) -> int:
        """returns -1 if it is not found"""
        for i, word in enumerate(self.dictionnary):
            if word.word == searched_word:
                return i
            
        return -1

    def from_json(self, json_file) -> list[Token]:
        data = json.loads(json_file)
        tokens = []

        for token_dict in data:
            tokens.append(Token.from_dict(token_dict))

        return tokens
    
    def predict_next_word(self):
        last_idx = self.idx_of_word_in_dict(self.last_word)

        if last_idx == -1:
            raise ValueError(f'word {self.last_word} not found')
        
        if self.dictionnary[last_idx].next_words.__len__() == 0:
            self.finish_generation = True
            return ".\n"

        weights = [probability for _, probability in self.dictionnary[last_idx].next_words.values()]
        choices = random.choices(list(self.dictionnary[last_idx].next_words.keys()), weights)
        if choices == []:
            self.finish_generation = True
            return ".\n"
        
        #print(choices)
        next_idx = int(random.choice(choices))

        next_word = self.dictionnary[next_idx].word
        self.last_word = next_word

        return next_word

def main():
    bot = ChatBot()

    while not bot.finish_generation:
        print(bot.predict_next_word(), end=" ")

if __name__ == "__main__":
    main()