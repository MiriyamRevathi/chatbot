"""
Porter Stemmer Algorithm Implementation from Scratch.
"""

class PorterStemmer:
    """Standard Porter Stemming Algorithm for English."""

    def _is_consonant(self, word, i):
        cv = word[i]
        if cv in "aeiou":
            return False
        if cv == "y":
            if i == 0:
                return True
            else:
                return not self._is_consonant(word, i - 1)
        return True

    def _m(self, word):
        """Measure of a word (number of VC sequences)."""
        n = 0
        i = 0
        length = len(word)
        while True:
            if i >= length:
                return n
            if not self._is_consonant(word, i):
                break
            i += 1
        i += 1
        while True:
            while True:
                if i >= length:
                    return n
                if self._is_consonant(word, i):
                    break
                i += 1
            i += 1
            n += 1
            while True:
                if i >= length:
                    return n
                if not self._is_consonant(word, i):
                    break
                i += 1
            i += 1

    def _vowel_in_stem(self, word):
        for i in range(len(word)):
            if not self._is_consonant(word, i):
                return True
        return False

    def _double_consonant(self, word):
        if len(word) < 2:
            return False
        return (word[-1] == word[-2]) and self._is_consonant(word, len(word) - 1)

    def stem(self, word: str) -> str:
        """Stem a word to its root form."""
        word = word.lower().strip()
        if len(word) <= 2:
            return word

        # Step 1a
        if word.endswith("sses"):
            word = word[:-2]
        elif word.endswith("ies"):
            word = word[:-2]
        elif word.endswith("ss"):
            pass
        elif word.endswith("s"):
            word = word[:-1]

        # Step 1b
        flag = False
        if word.endswith("eed"):
            stem = word[:-3]
            if self._m(stem) > 0:
                word = stem + "ee"
        elif word.endswith("ed"):
            stem = word[:-2]
            if self._vowel_in_stem(stem):
                word = stem
                flag = True
        elif word.endswith("ing"):
            stem = word[:-3]
            if self._vowel_in_stem(stem):
                word = stem
                flag = True

        if flag:
            if word.endswith("at") or word.endswith("bl") or word.endswith("iz"):
                word += "e"
            elif self._double_consonant(word) and not (word.endswith("l") or word.endswith("s") or word.endswith("z")):
                word = word[:-1]
            elif self._m(word) == 1 and self._is_consonant(word, len(word) - 1):
                word += "e"

        return word

porter_stemmer = PorterStemmer()
