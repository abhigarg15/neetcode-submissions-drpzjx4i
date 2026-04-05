class WordDictionary:

    def __init__(self):
        self.mp = {}

    def addWord(self, word: str) -> None:
        self.mp[word] = True

    def search(self, word: str) -> bool:
        if word in self.mp:
            return True
        for key in self.mp:
            if len(key) != len(word):
                continue
            i = 0
            for c in key:
                if c == word[i] or word[i] == ".":
                    i+=1
                else:
                    break
            
            if len(word) == i:
                return True

        return False
