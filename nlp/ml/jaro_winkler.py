"""
Jaro-Winkler String Distance Calculator.
"""

class JaroWinklerDistance:
    """Jaro-Winkler Distance Calculator for String Similarity."""

    @staticmethod
    def jaro_distance(s1: str, s2: str) -> float:
        if s1 == s2: return 1.0
        len1, len2 = len(s1), len(s2)
        if len1 == 0 or len2 == 0: return 0.0

        match_distance = max(len1, len2) // 2 - 1
        s1_matches = [False] * len1
        s2_matches = [False] * len2

        matches = 0
        transpositions = 0

        for i in range(len1):
            start = max(0, i - match_distance)
            end = min(i + match_distance + 1, len2)
            for j in range(start, end):
                if s2_matches[j]: continue
                if s1[i] != s2[j]: continue
                s1_matches[i] = True
                s2_matches[j] = True
                matches += 1
                break

        if matches == 0: return 0.0

        k = 0
        for i in range(len1):
            if not s1_matches[i]: continue
            while not s2_matches[k]: k += 1
            if s1[i] != s2[k]: transpositions += 1
            k += 1

        m = matches
        return (m / len1 + m / len2 + (m - transpositions / 2) / m) / 3.0

    @classmethod
    def distance(cls, s1: str, s2: str, p: float = 0.1) -> float:
        jaro = cls.jaro_distance(s1, s2)
        prefix = 0
        for c1, c2 in zip(s1, s2):
            if c1 == c2: prefix += 1
            else: break
            if prefix == 4: break
        return round(jaro + prefix * p * (1.0 - jaro), 4)

jaro_winkler = JaroWinklerDistance()
