class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        words = set(wordList)
        q = deque([(beginWord, 1)])
        while q:
            word,step = q.popleft()
            if word == endWord:
                return step
            for i,char in enumerate(word):
                for c in range(97,123):
                    if chr(c) == char:
                        continue 
                    new_word = word[:i] + chr(c) + word[i+1:]
                    if new_word in words:
                        words.remove(new_word)
                        q.append([new_word,step+1])
        return 0