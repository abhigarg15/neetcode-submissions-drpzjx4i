class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = set()


        def dfs(i,j,node,word):
            if (i,j) in visited or board[i][j] not in node.children :
                return 

            visited.add((i,j))
            node = node.children[board[i][j]]
            word+=board[i][j]
            if node.isWord:
                res.add(word)

            for ni,nj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if 0<=ni<ROWS and 0<=nj<COLS:
                    dfs(ni,nj,node,word)

            visited.remove((i,j))



        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)