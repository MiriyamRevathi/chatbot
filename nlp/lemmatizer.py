"""
Morphological Lemmatizer using Dictionary Rules.
"""

LEMMA_DICT = {
    "running": "run", "ran": "run", "runs": "run",
    "better": "good", "best": "good",
    "billing": "bill", "bills": "bill", "billed": "bill",
    "charged": "charge", "charges": "charge", "charging": "charge", "recharged": "charge",
    "requested": "request", "requesting": "request", "requests": "request",
    "refunded": "refund", "refunding": "refund", "refunds": "refund",
    "canceled": "cancel", "cancelling": "cancel", "cancels": "cancel", "cancellation": "cancel",
    "upgraded": "upgrade", "upgrading": "upgrade", "upgrades": "upgrade",
    "shipped": "ship", "shipping": "ship", "ships": "ship",
    "failed": "fail", "failing": "fail", "fails": "fail", "failure": "fail"
}

class Lemmatizer:
    """Dictionary and Rule Based Lemmatizer."""

    @staticmethod
    def lemmatize(word: str) -> str:
        """Lemmatize word to dictionary canonical form."""
        w = word.lower().strip()
        if w in LEMMA_DICT:
            return LEMMA_DICT[w]
        # Basic suffix rule heuristics
        if w.endswith("ing") and len(w) > 4:
            return w[:-3]
        if w.endswith("ed") and len(w) > 4:
            return w[:-2]
        if w.endswith("es") and len(w) > 3:
            return w[:-2]
        if w.endswith("s") and len(w) > 3 and not w.endswith("ss"):
            return w[:-1]
        return w

lemmatizer = Lemmatizer()
