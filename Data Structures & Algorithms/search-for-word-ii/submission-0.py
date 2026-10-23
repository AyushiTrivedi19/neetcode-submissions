class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        
        row = len(board)
        col = len(board[0])
        res = set()

        def dfs(r, c, node):
            if (r<0 or r>=row or c<0 or c>=col or board[r][c] not in node.children):
                return
            ch = board[r][c]
            nextNode = node.children[ch]
            
            if nextNode.word is not None:
                res.add(nextNode.word)

            board[r][c] = "#"
            dfs(r+1, c, nextNode)
            dfs(r-1, c, nextNode)
            dfs(r, c+1, nextNode)
            dfs(r, c-1, nextNode)

            board[r][c] = ch
        
        for r in range(row):
            for c in range(col):
                dfs(r,c, self.root)
        
        return list(res)

        