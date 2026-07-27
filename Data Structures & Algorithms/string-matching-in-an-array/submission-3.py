class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matchingWords = set()

        words.sort(key=len)

        for i in range(len(words)):

            for word in words[i+1:]:
                if words[i] in word:
                    matchingWords.add(words[i])

        return list(matchingWords)
        