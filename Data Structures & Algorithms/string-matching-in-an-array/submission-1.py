class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matchingWords = set()

        for i in range(len(words)):

            for word in words[i+1:]:
                if word in words[i]:
                    matchingWords.add(word)
                elif words[i] in word:
                    matchingWords.add(words[i])



        return list(matchingWords)
        