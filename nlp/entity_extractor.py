"""
Master Named Entity Recognition Engine.
Combines Regex and Gazetteer Entity Extractors.
"""

from nlp.regex_entities import regex_entity_extractor
from nlp.gazetteer import gazetteer_extractor

class EntityExtractor:
    """Master Entity Extractor."""

    def extract_entities(self, text: str) -> list:
        """Extract all entities from text."""
        if not text:
            return []

        regex_ents = regex_entity_extractor.extract(text)
        gaz_ents = gazetteer_extractor.extract(text)

        all_ents = regex_ents + gaz_ents
        return all_ents

entity_extractor = EntityExtractor()
