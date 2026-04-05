class WordDictionary:

    def __init__(self):
        self.mp = {}        

    def addWord(self, word: str) -> None:
        self.mp[word] = True

    def search(self, word: str) -> bool:
        if word in self.mp:
            return True

        for listWords in self.mp: # keys
            if len(listWords) != len(word):
                continue
            i = 0
            for c in listWords:
                if c == word[i] or word[i] == ".":
                    i+=1
                else:
                    break
            if i == len(word):
                return True

        return False

        
