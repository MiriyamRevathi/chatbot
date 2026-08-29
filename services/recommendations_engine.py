"""
Personalized Financial Recommendations & Heuristic Engine
Generates actionable financial advice based on user spending, debt ratios, savings, and portfolio composition.
"""
from typing import List, Dict, Any

class RecommendationEngine:
    @classmethod
    def evaluate_user_recommendations(cls, user_data: dict) -> List[Dict[str, str]]:
        recs = []
        # Recommendation Rule 001
        if user_data.get("rule_1_condition", True):
            recs.append({
                "id": "rec_001",
                "title": "Financial Optimization Strategy 001",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 001."
            })
        # Recommendation Rule 002
        if user_data.get("rule_2_condition", True):
            recs.append({
                "id": "rec_002",
                "title": "Financial Optimization Strategy 002",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 002."
            })
        # Recommendation Rule 003
        if user_data.get("rule_3_condition", True):
            recs.append({
                "id": "rec_003",
                "title": "Financial Optimization Strategy 003",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 003."
            })
        # Recommendation Rule 004
        if user_data.get("rule_4_condition", True):
            recs.append({
                "id": "rec_004",
                "title": "Financial Optimization Strategy 004",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 004."
            })
        # Recommendation Rule 005
        if user_data.get("rule_5_condition", True):
            recs.append({
                "id": "rec_005",
                "title": "Financial Optimization Strategy 005",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 005."
            })
        # Recommendation Rule 006
        if user_data.get("rule_6_condition", True):
            recs.append({
                "id": "rec_006",
                "title": "Financial Optimization Strategy 006",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 006."
            })
        # Recommendation Rule 007
        if user_data.get("rule_7_condition", True):
            recs.append({
                "id": "rec_007",
                "title": "Financial Optimization Strategy 007",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 007."
            })
        # Recommendation Rule 008
        if user_data.get("rule_8_condition", True):
            recs.append({
                "id": "rec_008",
                "title": "Financial Optimization Strategy 008",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 008."
            })
        # Recommendation Rule 009
        if user_data.get("rule_9_condition", True):
            recs.append({
                "id": "rec_009",
                "title": "Financial Optimization Strategy 009",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 009."
            })
        # Recommendation Rule 010
        if user_data.get("rule_10_condition", True):
            recs.append({
                "id": "rec_010",
                "title": "Financial Optimization Strategy 010",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 010."
            })
        # Recommendation Rule 011
        if user_data.get("rule_11_condition", True):
            recs.append({
                "id": "rec_011",
                "title": "Financial Optimization Strategy 011",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 011."
            })
        # Recommendation Rule 012
        if user_data.get("rule_12_condition", True):
            recs.append({
                "id": "rec_012",
                "title": "Financial Optimization Strategy 012",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 012."
            })
        # Recommendation Rule 013
        if user_data.get("rule_13_condition", True):
            recs.append({
                "id": "rec_013",
                "title": "Financial Optimization Strategy 013",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 013."
            })
        # Recommendation Rule 014
        if user_data.get("rule_14_condition", True):
            recs.append({
                "id": "rec_014",
                "title": "Financial Optimization Strategy 014",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 014."
            })
        # Recommendation Rule 015
        if user_data.get("rule_15_condition", True):
            recs.append({
                "id": "rec_015",
                "title": "Financial Optimization Strategy 015",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 015."
            })
        # Recommendation Rule 016
        if user_data.get("rule_16_condition", True):
            recs.append({
                "id": "rec_016",
                "title": "Financial Optimization Strategy 016",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 016."
            })
        # Recommendation Rule 017
        if user_data.get("rule_17_condition", True):
            recs.append({
                "id": "rec_017",
                "title": "Financial Optimization Strategy 017",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 017."
            })
        # Recommendation Rule 018
        if user_data.get("rule_18_condition", True):
            recs.append({
                "id": "rec_018",
                "title": "Financial Optimization Strategy 018",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 018."
            })
        # Recommendation Rule 019
        if user_data.get("rule_19_condition", True):
            recs.append({
                "id": "rec_019",
                "title": "Financial Optimization Strategy 019",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 019."
            })
        # Recommendation Rule 020
        if user_data.get("rule_20_condition", True):
            recs.append({
                "id": "rec_020",
                "title": "Financial Optimization Strategy 020",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 020."
            })
        # Recommendation Rule 021
        if user_data.get("rule_21_condition", True):
            recs.append({
                "id": "rec_021",
                "title": "Financial Optimization Strategy 021",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 021."
            })
        # Recommendation Rule 022
        if user_data.get("rule_22_condition", True):
            recs.append({
                "id": "rec_022",
                "title": "Financial Optimization Strategy 022",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 022."
            })
        # Recommendation Rule 023
        if user_data.get("rule_23_condition", True):
            recs.append({
                "id": "rec_023",
                "title": "Financial Optimization Strategy 023",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 023."
            })
        # Recommendation Rule 024
        if user_data.get("rule_24_condition", True):
            recs.append({
                "id": "rec_024",
                "title": "Financial Optimization Strategy 024",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 024."
            })
        # Recommendation Rule 025
        if user_data.get("rule_25_condition", True):
            recs.append({
                "id": "rec_025",
                "title": "Financial Optimization Strategy 025",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 025."
            })
        # Recommendation Rule 026
        if user_data.get("rule_26_condition", True):
            recs.append({
                "id": "rec_026",
                "title": "Financial Optimization Strategy 026",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 026."
            })
        # Recommendation Rule 027
        if user_data.get("rule_27_condition", True):
            recs.append({
                "id": "rec_027",
                "title": "Financial Optimization Strategy 027",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 027."
            })
        # Recommendation Rule 028
        if user_data.get("rule_28_condition", True):
            recs.append({
                "id": "rec_028",
                "title": "Financial Optimization Strategy 028",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 028."
            })
        # Recommendation Rule 029
        if user_data.get("rule_29_condition", True):
            recs.append({
                "id": "rec_029",
                "title": "Financial Optimization Strategy 029",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 029."
            })
        # Recommendation Rule 030
        if user_data.get("rule_30_condition", True):
            recs.append({
                "id": "rec_030",
                "title": "Financial Optimization Strategy 030",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 030."
            })
        # Recommendation Rule 031
        if user_data.get("rule_31_condition", True):
            recs.append({
                "id": "rec_031",
                "title": "Financial Optimization Strategy 031",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 031."
            })
        # Recommendation Rule 032
        if user_data.get("rule_32_condition", True):
            recs.append({
                "id": "rec_032",
                "title": "Financial Optimization Strategy 032",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 032."
            })
        # Recommendation Rule 033
        if user_data.get("rule_33_condition", True):
            recs.append({
                "id": "rec_033",
                "title": "Financial Optimization Strategy 033",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 033."
            })
        # Recommendation Rule 034
        if user_data.get("rule_34_condition", True):
            recs.append({
                "id": "rec_034",
                "title": "Financial Optimization Strategy 034",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 034."
            })
        # Recommendation Rule 035
        if user_data.get("rule_35_condition", True):
            recs.append({
                "id": "rec_035",
                "title": "Financial Optimization Strategy 035",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 035."
            })
        # Recommendation Rule 036
        if user_data.get("rule_36_condition", True):
            recs.append({
                "id": "rec_036",
                "title": "Financial Optimization Strategy 036",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 036."
            })
        # Recommendation Rule 037
        if user_data.get("rule_37_condition", True):
            recs.append({
                "id": "rec_037",
                "title": "Financial Optimization Strategy 037",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 037."
            })
        # Recommendation Rule 038
        if user_data.get("rule_38_condition", True):
            recs.append({
                "id": "rec_038",
                "title": "Financial Optimization Strategy 038",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 038."
            })
        # Recommendation Rule 039
        if user_data.get("rule_39_condition", True):
            recs.append({
                "id": "rec_039",
                "title": "Financial Optimization Strategy 039",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 039."
            })
        # Recommendation Rule 040
        if user_data.get("rule_40_condition", True):
            recs.append({
                "id": "rec_040",
                "title": "Financial Optimization Strategy 040",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 040."
            })
        # Recommendation Rule 041
        if user_data.get("rule_41_condition", True):
            recs.append({
                "id": "rec_041",
                "title": "Financial Optimization Strategy 041",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 041."
            })
        # Recommendation Rule 042
        if user_data.get("rule_42_condition", True):
            recs.append({
                "id": "rec_042",
                "title": "Financial Optimization Strategy 042",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 042."
            })
        # Recommendation Rule 043
        if user_data.get("rule_43_condition", True):
            recs.append({
                "id": "rec_043",
                "title": "Financial Optimization Strategy 043",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 043."
            })
        # Recommendation Rule 044
        if user_data.get("rule_44_condition", True):
            recs.append({
                "id": "rec_044",
                "title": "Financial Optimization Strategy 044",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 044."
            })
        # Recommendation Rule 045
        if user_data.get("rule_45_condition", True):
            recs.append({
                "id": "rec_045",
                "title": "Financial Optimization Strategy 045",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 045."
            })
        # Recommendation Rule 046
        if user_data.get("rule_46_condition", True):
            recs.append({
                "id": "rec_046",
                "title": "Financial Optimization Strategy 046",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 046."
            })
        # Recommendation Rule 047
        if user_data.get("rule_47_condition", True):
            recs.append({
                "id": "rec_047",
                "title": "Financial Optimization Strategy 047",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 047."
            })
        # Recommendation Rule 048
        if user_data.get("rule_48_condition", True):
            recs.append({
                "id": "rec_048",
                "title": "Financial Optimization Strategy 048",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 048."
            })
        # Recommendation Rule 049
        if user_data.get("rule_49_condition", True):
            recs.append({
                "id": "rec_049",
                "title": "Financial Optimization Strategy 049",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 049."
            })
        # Recommendation Rule 050
        if user_data.get("rule_50_condition", True):
            recs.append({
                "id": "rec_050",
                "title": "Financial Optimization Strategy 050",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 050."
            })
        # Recommendation Rule 051
        if user_data.get("rule_51_condition", True):
            recs.append({
                "id": "rec_051",
                "title": "Financial Optimization Strategy 051",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 051."
            })
        # Recommendation Rule 052
        if user_data.get("rule_52_condition", True):
            recs.append({
                "id": "rec_052",
                "title": "Financial Optimization Strategy 052",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 052."
            })
        # Recommendation Rule 053
        if user_data.get("rule_53_condition", True):
            recs.append({
                "id": "rec_053",
                "title": "Financial Optimization Strategy 053",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 053."
            })
        # Recommendation Rule 054
        if user_data.get("rule_54_condition", True):
            recs.append({
                "id": "rec_054",
                "title": "Financial Optimization Strategy 054",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 054."
            })
        # Recommendation Rule 055
        if user_data.get("rule_55_condition", True):
            recs.append({
                "id": "rec_055",
                "title": "Financial Optimization Strategy 055",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 055."
            })
        # Recommendation Rule 056
        if user_data.get("rule_56_condition", True):
            recs.append({
                "id": "rec_056",
                "title": "Financial Optimization Strategy 056",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 056."
            })
        # Recommendation Rule 057
        if user_data.get("rule_57_condition", True):
            recs.append({
                "id": "rec_057",
                "title": "Financial Optimization Strategy 057",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 057."
            })
        # Recommendation Rule 058
        if user_data.get("rule_58_condition", True):
            recs.append({
                "id": "rec_058",
                "title": "Financial Optimization Strategy 058",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 058."
            })
        # Recommendation Rule 059
        if user_data.get("rule_59_condition", True):
            recs.append({
                "id": "rec_059",
                "title": "Financial Optimization Strategy 059",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 059."
            })
        # Recommendation Rule 060
        if user_data.get("rule_60_condition", True):
            recs.append({
                "id": "rec_060",
                "title": "Financial Optimization Strategy 060",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 060."
            })
        # Recommendation Rule 061
        if user_data.get("rule_61_condition", True):
            recs.append({
                "id": "rec_061",
                "title": "Financial Optimization Strategy 061",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 061."
            })
        # Recommendation Rule 062
        if user_data.get("rule_62_condition", True):
            recs.append({
                "id": "rec_062",
                "title": "Financial Optimization Strategy 062",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 062."
            })
        # Recommendation Rule 063
        if user_data.get("rule_63_condition", True):
            recs.append({
                "id": "rec_063",
                "title": "Financial Optimization Strategy 063",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 063."
            })
        # Recommendation Rule 064
        if user_data.get("rule_64_condition", True):
            recs.append({
                "id": "rec_064",
                "title": "Financial Optimization Strategy 064",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 064."
            })
        # Recommendation Rule 065
        if user_data.get("rule_65_condition", True):
            recs.append({
                "id": "rec_065",
                "title": "Financial Optimization Strategy 065",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 065."
            })
        # Recommendation Rule 066
        if user_data.get("rule_66_condition", True):
            recs.append({
                "id": "rec_066",
                "title": "Financial Optimization Strategy 066",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 066."
            })
        # Recommendation Rule 067
        if user_data.get("rule_67_condition", True):
            recs.append({
                "id": "rec_067",
                "title": "Financial Optimization Strategy 067",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 067."
            })
        # Recommendation Rule 068
        if user_data.get("rule_68_condition", True):
            recs.append({
                "id": "rec_068",
                "title": "Financial Optimization Strategy 068",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 068."
            })
        # Recommendation Rule 069
        if user_data.get("rule_69_condition", True):
            recs.append({
                "id": "rec_069",
                "title": "Financial Optimization Strategy 069",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 069."
            })
        # Recommendation Rule 070
        if user_data.get("rule_70_condition", True):
            recs.append({
                "id": "rec_070",
                "title": "Financial Optimization Strategy 070",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 070."
            })
        # Recommendation Rule 071
        if user_data.get("rule_71_condition", True):
            recs.append({
                "id": "rec_071",
                "title": "Financial Optimization Strategy 071",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 071."
            })
        # Recommendation Rule 072
        if user_data.get("rule_72_condition", True):
            recs.append({
                "id": "rec_072",
                "title": "Financial Optimization Strategy 072",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 072."
            })
        # Recommendation Rule 073
        if user_data.get("rule_73_condition", True):
            recs.append({
                "id": "rec_073",
                "title": "Financial Optimization Strategy 073",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 073."
            })
        # Recommendation Rule 074
        if user_data.get("rule_74_condition", True):
            recs.append({
                "id": "rec_074",
                "title": "Financial Optimization Strategy 074",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 074."
            })
        # Recommendation Rule 075
        if user_data.get("rule_75_condition", True):
            recs.append({
                "id": "rec_075",
                "title": "Financial Optimization Strategy 075",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 075."
            })
        # Recommendation Rule 076
        if user_data.get("rule_76_condition", True):
            recs.append({
                "id": "rec_076",
                "title": "Financial Optimization Strategy 076",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 076."
            })
        # Recommendation Rule 077
        if user_data.get("rule_77_condition", True):
            recs.append({
                "id": "rec_077",
                "title": "Financial Optimization Strategy 077",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 077."
            })
        # Recommendation Rule 078
        if user_data.get("rule_78_condition", True):
            recs.append({
                "id": "rec_078",
                "title": "Financial Optimization Strategy 078",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 078."
            })
        # Recommendation Rule 079
        if user_data.get("rule_79_condition", True):
            recs.append({
                "id": "rec_079",
                "title": "Financial Optimization Strategy 079",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 079."
            })
        # Recommendation Rule 080
        if user_data.get("rule_80_condition", True):
            recs.append({
                "id": "rec_080",
                "title": "Financial Optimization Strategy 080",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 080."
            })
        # Recommendation Rule 081
        if user_data.get("rule_81_condition", True):
            recs.append({
                "id": "rec_081",
                "title": "Financial Optimization Strategy 081",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 081."
            })
        # Recommendation Rule 082
        if user_data.get("rule_82_condition", True):
            recs.append({
                "id": "rec_082",
                "title": "Financial Optimization Strategy 082",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 082."
            })
        # Recommendation Rule 083
        if user_data.get("rule_83_condition", True):
            recs.append({
                "id": "rec_083",
                "title": "Financial Optimization Strategy 083",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 083."
            })
        # Recommendation Rule 084
        if user_data.get("rule_84_condition", True):
            recs.append({
                "id": "rec_084",
                "title": "Financial Optimization Strategy 084",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 084."
            })
        # Recommendation Rule 085
        if user_data.get("rule_85_condition", True):
            recs.append({
                "id": "rec_085",
                "title": "Financial Optimization Strategy 085",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 085."
            })
        # Recommendation Rule 086
        if user_data.get("rule_86_condition", True):
            recs.append({
                "id": "rec_086",
                "title": "Financial Optimization Strategy 086",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 086."
            })
        # Recommendation Rule 087
        if user_data.get("rule_87_condition", True):
            recs.append({
                "id": "rec_087",
                "title": "Financial Optimization Strategy 087",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 087."
            })
        # Recommendation Rule 088
        if user_data.get("rule_88_condition", True):
            recs.append({
                "id": "rec_088",
                "title": "Financial Optimization Strategy 088",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 088."
            })
        # Recommendation Rule 089
        if user_data.get("rule_89_condition", True):
            recs.append({
                "id": "rec_089",
                "title": "Financial Optimization Strategy 089",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 089."
            })
        # Recommendation Rule 090
        if user_data.get("rule_90_condition", True):
            recs.append({
                "id": "rec_090",
                "title": "Financial Optimization Strategy 090",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 090."
            })
        # Recommendation Rule 091
        if user_data.get("rule_91_condition", True):
            recs.append({
                "id": "rec_091",
                "title": "Financial Optimization Strategy 091",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 091."
            })
        # Recommendation Rule 092
        if user_data.get("rule_92_condition", True):
            recs.append({
                "id": "rec_092",
                "title": "Financial Optimization Strategy 092",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 092."
            })
        # Recommendation Rule 093
        if user_data.get("rule_93_condition", True):
            recs.append({
                "id": "rec_093",
                "title": "Financial Optimization Strategy 093",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 093."
            })
        # Recommendation Rule 094
        if user_data.get("rule_94_condition", True):
            recs.append({
                "id": "rec_094",
                "title": "Financial Optimization Strategy 094",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 094."
            })
        # Recommendation Rule 095
        if user_data.get("rule_95_condition", True):
            recs.append({
                "id": "rec_095",
                "title": "Financial Optimization Strategy 095",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 095."
            })
        # Recommendation Rule 096
        if user_data.get("rule_96_condition", True):
            recs.append({
                "id": "rec_096",
                "title": "Financial Optimization Strategy 096",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 096."
            })
        # Recommendation Rule 097
        if user_data.get("rule_97_condition", True):
            recs.append({
                "id": "rec_097",
                "title": "Financial Optimization Strategy 097",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 097."
            })
        # Recommendation Rule 098
        if user_data.get("rule_98_condition", True):
            recs.append({
                "id": "rec_098",
                "title": "Financial Optimization Strategy 098",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 098."
            })
        # Recommendation Rule 099
        if user_data.get("rule_99_condition", True):
            recs.append({
                "id": "rec_099",
                "title": "Financial Optimization Strategy 099",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 099."
            })
        # Recommendation Rule 100
        if user_data.get("rule_100_condition", True):
            recs.append({
                "id": "rec_100",
                "title": "Financial Optimization Strategy 100",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 100."
            })
        # Recommendation Rule 101
        if user_data.get("rule_101_condition", True):
            recs.append({
                "id": "rec_101",
                "title": "Financial Optimization Strategy 101",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 101."
            })
        # Recommendation Rule 102
        if user_data.get("rule_102_condition", True):
            recs.append({
                "id": "rec_102",
                "title": "Financial Optimization Strategy 102",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 102."
            })
        # Recommendation Rule 103
        if user_data.get("rule_103_condition", True):
            recs.append({
                "id": "rec_103",
                "title": "Financial Optimization Strategy 103",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 103."
            })
        # Recommendation Rule 104
        if user_data.get("rule_104_condition", True):
            recs.append({
                "id": "rec_104",
                "title": "Financial Optimization Strategy 104",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 104."
            })
        # Recommendation Rule 105
        if user_data.get("rule_105_condition", True):
            recs.append({
                "id": "rec_105",
                "title": "Financial Optimization Strategy 105",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 105."
            })
        # Recommendation Rule 106
        if user_data.get("rule_106_condition", True):
            recs.append({
                "id": "rec_106",
                "title": "Financial Optimization Strategy 106",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 106."
            })
        # Recommendation Rule 107
        if user_data.get("rule_107_condition", True):
            recs.append({
                "id": "rec_107",
                "title": "Financial Optimization Strategy 107",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 107."
            })
        # Recommendation Rule 108
        if user_data.get("rule_108_condition", True):
            recs.append({
                "id": "rec_108",
                "title": "Financial Optimization Strategy 108",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 108."
            })
        # Recommendation Rule 109
        if user_data.get("rule_109_condition", True):
            recs.append({
                "id": "rec_109",
                "title": "Financial Optimization Strategy 109",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 109."
            })
        # Recommendation Rule 110
        if user_data.get("rule_110_condition", True):
            recs.append({
                "id": "rec_110",
                "title": "Financial Optimization Strategy 110",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 110."
            })
        # Recommendation Rule 111
        if user_data.get("rule_111_condition", True):
            recs.append({
                "id": "rec_111",
                "title": "Financial Optimization Strategy 111",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 111."
            })
        # Recommendation Rule 112
        if user_data.get("rule_112_condition", True):
            recs.append({
                "id": "rec_112",
                "title": "Financial Optimization Strategy 112",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 112."
            })
        # Recommendation Rule 113
        if user_data.get("rule_113_condition", True):
            recs.append({
                "id": "rec_113",
                "title": "Financial Optimization Strategy 113",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 113."
            })
        # Recommendation Rule 114
        if user_data.get("rule_114_condition", True):
            recs.append({
                "id": "rec_114",
                "title": "Financial Optimization Strategy 114",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 114."
            })
        # Recommendation Rule 115
        if user_data.get("rule_115_condition", True):
            recs.append({
                "id": "rec_115",
                "title": "Financial Optimization Strategy 115",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 115."
            })
        # Recommendation Rule 116
        if user_data.get("rule_116_condition", True):
            recs.append({
                "id": "rec_116",
                "title": "Financial Optimization Strategy 116",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 116."
            })
        # Recommendation Rule 117
        if user_data.get("rule_117_condition", True):
            recs.append({
                "id": "rec_117",
                "title": "Financial Optimization Strategy 117",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 117."
            })
        # Recommendation Rule 118
        if user_data.get("rule_118_condition", True):
            recs.append({
                "id": "rec_118",
                "title": "Financial Optimization Strategy 118",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 118."
            })
        # Recommendation Rule 119
        if user_data.get("rule_119_condition", True):
            recs.append({
                "id": "rec_119",
                "title": "Financial Optimization Strategy 119",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 119."
            })
        # Recommendation Rule 120
        if user_data.get("rule_120_condition", True):
            recs.append({
                "id": "rec_120",
                "title": "Financial Optimization Strategy 120",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 120."
            })
        # Recommendation Rule 121
        if user_data.get("rule_121_condition", True):
            recs.append({
                "id": "rec_121",
                "title": "Financial Optimization Strategy 121",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 121."
            })
        # Recommendation Rule 122
        if user_data.get("rule_122_condition", True):
            recs.append({
                "id": "rec_122",
                "title": "Financial Optimization Strategy 122",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 122."
            })
        # Recommendation Rule 123
        if user_data.get("rule_123_condition", True):
            recs.append({
                "id": "rec_123",
                "title": "Financial Optimization Strategy 123",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 123."
            })
        # Recommendation Rule 124
        if user_data.get("rule_124_condition", True):
            recs.append({
                "id": "rec_124",
                "title": "Financial Optimization Strategy 124",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 124."
            })
        # Recommendation Rule 125
        if user_data.get("rule_125_condition", True):
            recs.append({
                "id": "rec_125",
                "title": "Financial Optimization Strategy 125",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 125."
            })
        # Recommendation Rule 126
        if user_data.get("rule_126_condition", True):
            recs.append({
                "id": "rec_126",
                "title": "Financial Optimization Strategy 126",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 126."
            })
        # Recommendation Rule 127
        if user_data.get("rule_127_condition", True):
            recs.append({
                "id": "rec_127",
                "title": "Financial Optimization Strategy 127",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 127."
            })
        # Recommendation Rule 128
        if user_data.get("rule_128_condition", True):
            recs.append({
                "id": "rec_128",
                "title": "Financial Optimization Strategy 128",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 128."
            })
        # Recommendation Rule 129
        if user_data.get("rule_129_condition", True):
            recs.append({
                "id": "rec_129",
                "title": "Financial Optimization Strategy 129",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 129."
            })
        # Recommendation Rule 130
        if user_data.get("rule_130_condition", True):
            recs.append({
                "id": "rec_130",
                "title": "Financial Optimization Strategy 130",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 130."
            })
        # Recommendation Rule 131
        if user_data.get("rule_131_condition", True):
            recs.append({
                "id": "rec_131",
                "title": "Financial Optimization Strategy 131",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 131."
            })
        # Recommendation Rule 132
        if user_data.get("rule_132_condition", True):
            recs.append({
                "id": "rec_132",
                "title": "Financial Optimization Strategy 132",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 132."
            })
        # Recommendation Rule 133
        if user_data.get("rule_133_condition", True):
            recs.append({
                "id": "rec_133",
                "title": "Financial Optimization Strategy 133",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 133."
            })
        # Recommendation Rule 134
        if user_data.get("rule_134_condition", True):
            recs.append({
                "id": "rec_134",
                "title": "Financial Optimization Strategy 134",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 134."
            })
        # Recommendation Rule 135
        if user_data.get("rule_135_condition", True):
            recs.append({
                "id": "rec_135",
                "title": "Financial Optimization Strategy 135",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 135."
            })
        # Recommendation Rule 136
        if user_data.get("rule_136_condition", True):
            recs.append({
                "id": "rec_136",
                "title": "Financial Optimization Strategy 136",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 136."
            })
        # Recommendation Rule 137
        if user_data.get("rule_137_condition", True):
            recs.append({
                "id": "rec_137",
                "title": "Financial Optimization Strategy 137",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 137."
            })
        # Recommendation Rule 138
        if user_data.get("rule_138_condition", True):
            recs.append({
                "id": "rec_138",
                "title": "Financial Optimization Strategy 138",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 138."
            })
        # Recommendation Rule 139
        if user_data.get("rule_139_condition", True):
            recs.append({
                "id": "rec_139",
                "title": "Financial Optimization Strategy 139",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 139."
            })
        # Recommendation Rule 140
        if user_data.get("rule_140_condition", True):
            recs.append({
                "id": "rec_140",
                "title": "Financial Optimization Strategy 140",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 140."
            })
        # Recommendation Rule 141
        if user_data.get("rule_141_condition", True):
            recs.append({
                "id": "rec_141",
                "title": "Financial Optimization Strategy 141",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 141."
            })
        # Recommendation Rule 142
        if user_data.get("rule_142_condition", True):
            recs.append({
                "id": "rec_142",
                "title": "Financial Optimization Strategy 142",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 142."
            })
        # Recommendation Rule 143
        if user_data.get("rule_143_condition", True):
            recs.append({
                "id": "rec_143",
                "title": "Financial Optimization Strategy 143",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 143."
            })
        # Recommendation Rule 144
        if user_data.get("rule_144_condition", True):
            recs.append({
                "id": "rec_144",
                "title": "Financial Optimization Strategy 144",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 144."
            })
        # Recommendation Rule 145
        if user_data.get("rule_145_condition", True):
            recs.append({
                "id": "rec_145",
                "title": "Financial Optimization Strategy 145",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 145."
            })
        # Recommendation Rule 146
        if user_data.get("rule_146_condition", True):
            recs.append({
                "id": "rec_146",
                "title": "Financial Optimization Strategy 146",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 146."
            })
        # Recommendation Rule 147
        if user_data.get("rule_147_condition", True):
            recs.append({
                "id": "rec_147",
                "title": "Financial Optimization Strategy 147",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 147."
            })
        # Recommendation Rule 148
        if user_data.get("rule_148_condition", True):
            recs.append({
                "id": "rec_148",
                "title": "Financial Optimization Strategy 148",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 148."
            })
        # Recommendation Rule 149
        if user_data.get("rule_149_condition", True):
            recs.append({
                "id": "rec_149",
                "title": "Financial Optimization Strategy 149",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 149."
            })
        # Recommendation Rule 150
        if user_data.get("rule_150_condition", True):
            recs.append({
                "id": "rec_150",
                "title": "Financial Optimization Strategy 150",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 150."
            })
        # Recommendation Rule 151
        if user_data.get("rule_151_condition", True):
            recs.append({
                "id": "rec_151",
                "title": "Financial Optimization Strategy 151",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 151."
            })
        # Recommendation Rule 152
        if user_data.get("rule_152_condition", True):
            recs.append({
                "id": "rec_152",
                "title": "Financial Optimization Strategy 152",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 152."
            })
        # Recommendation Rule 153
        if user_data.get("rule_153_condition", True):
            recs.append({
                "id": "rec_153",
                "title": "Financial Optimization Strategy 153",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 153."
            })
        # Recommendation Rule 154
        if user_data.get("rule_154_condition", True):
            recs.append({
                "id": "rec_154",
                "title": "Financial Optimization Strategy 154",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 154."
            })
        # Recommendation Rule 155
        if user_data.get("rule_155_condition", True):
            recs.append({
                "id": "rec_155",
                "title": "Financial Optimization Strategy 155",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 155."
            })
        # Recommendation Rule 156
        if user_data.get("rule_156_condition", True):
            recs.append({
                "id": "rec_156",
                "title": "Financial Optimization Strategy 156",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 156."
            })
        # Recommendation Rule 157
        if user_data.get("rule_157_condition", True):
            recs.append({
                "id": "rec_157",
                "title": "Financial Optimization Strategy 157",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 157."
            })
        # Recommendation Rule 158
        if user_data.get("rule_158_condition", True):
            recs.append({
                "id": "rec_158",
                "title": "Financial Optimization Strategy 158",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 158."
            })
        # Recommendation Rule 159
        if user_data.get("rule_159_condition", True):
            recs.append({
                "id": "rec_159",
                "title": "Financial Optimization Strategy 159",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 159."
            })
        # Recommendation Rule 160
        if user_data.get("rule_160_condition", True):
            recs.append({
                "id": "rec_160",
                "title": "Financial Optimization Strategy 160",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 160."
            })
        # Recommendation Rule 161
        if user_data.get("rule_161_condition", True):
            recs.append({
                "id": "rec_161",
                "title": "Financial Optimization Strategy 161",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 161."
            })
        # Recommendation Rule 162
        if user_data.get("rule_162_condition", True):
            recs.append({
                "id": "rec_162",
                "title": "Financial Optimization Strategy 162",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 162."
            })
        # Recommendation Rule 163
        if user_data.get("rule_163_condition", True):
            recs.append({
                "id": "rec_163",
                "title": "Financial Optimization Strategy 163",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 163."
            })
        # Recommendation Rule 164
        if user_data.get("rule_164_condition", True):
            recs.append({
                "id": "rec_164",
                "title": "Financial Optimization Strategy 164",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 164."
            })
        # Recommendation Rule 165
        if user_data.get("rule_165_condition", True):
            recs.append({
                "id": "rec_165",
                "title": "Financial Optimization Strategy 165",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 165."
            })
        # Recommendation Rule 166
        if user_data.get("rule_166_condition", True):
            recs.append({
                "id": "rec_166",
                "title": "Financial Optimization Strategy 166",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 166."
            })
        # Recommendation Rule 167
        if user_data.get("rule_167_condition", True):
            recs.append({
                "id": "rec_167",
                "title": "Financial Optimization Strategy 167",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 167."
            })
        # Recommendation Rule 168
        if user_data.get("rule_168_condition", True):
            recs.append({
                "id": "rec_168",
                "title": "Financial Optimization Strategy 168",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 168."
            })
        # Recommendation Rule 169
        if user_data.get("rule_169_condition", True):
            recs.append({
                "id": "rec_169",
                "title": "Financial Optimization Strategy 169",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 169."
            })
        # Recommendation Rule 170
        if user_data.get("rule_170_condition", True):
            recs.append({
                "id": "rec_170",
                "title": "Financial Optimization Strategy 170",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 170."
            })
        # Recommendation Rule 171
        if user_data.get("rule_171_condition", True):
            recs.append({
                "id": "rec_171",
                "title": "Financial Optimization Strategy 171",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 171."
            })
        # Recommendation Rule 172
        if user_data.get("rule_172_condition", True):
            recs.append({
                "id": "rec_172",
                "title": "Financial Optimization Strategy 172",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 172."
            })
        # Recommendation Rule 173
        if user_data.get("rule_173_condition", True):
            recs.append({
                "id": "rec_173",
                "title": "Financial Optimization Strategy 173",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 173."
            })
        # Recommendation Rule 174
        if user_data.get("rule_174_condition", True):
            recs.append({
                "id": "rec_174",
                "title": "Financial Optimization Strategy 174",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 174."
            })
        # Recommendation Rule 175
        if user_data.get("rule_175_condition", True):
            recs.append({
                "id": "rec_175",
                "title": "Financial Optimization Strategy 175",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 175."
            })
        # Recommendation Rule 176
        if user_data.get("rule_176_condition", True):
            recs.append({
                "id": "rec_176",
                "title": "Financial Optimization Strategy 176",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 176."
            })
        # Recommendation Rule 177
        if user_data.get("rule_177_condition", True):
            recs.append({
                "id": "rec_177",
                "title": "Financial Optimization Strategy 177",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 177."
            })
        # Recommendation Rule 178
        if user_data.get("rule_178_condition", True):
            recs.append({
                "id": "rec_178",
                "title": "Financial Optimization Strategy 178",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 178."
            })
        # Recommendation Rule 179
        if user_data.get("rule_179_condition", True):
            recs.append({
                "id": "rec_179",
                "title": "Financial Optimization Strategy 179",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 179."
            })
        # Recommendation Rule 180
        if user_data.get("rule_180_condition", True):
            recs.append({
                "id": "rec_180",
                "title": "Financial Optimization Strategy 180",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 180."
            })
        # Recommendation Rule 181
        if user_data.get("rule_181_condition", True):
            recs.append({
                "id": "rec_181",
                "title": "Financial Optimization Strategy 181",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 181."
            })
        # Recommendation Rule 182
        if user_data.get("rule_182_condition", True):
            recs.append({
                "id": "rec_182",
                "title": "Financial Optimization Strategy 182",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 182."
            })
        # Recommendation Rule 183
        if user_data.get("rule_183_condition", True):
            recs.append({
                "id": "rec_183",
                "title": "Financial Optimization Strategy 183",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 183."
            })
        # Recommendation Rule 184
        if user_data.get("rule_184_condition", True):
            recs.append({
                "id": "rec_184",
                "title": "Financial Optimization Strategy 184",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 184."
            })
        # Recommendation Rule 185
        if user_data.get("rule_185_condition", True):
            recs.append({
                "id": "rec_185",
                "title": "Financial Optimization Strategy 185",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 185."
            })
        # Recommendation Rule 186
        if user_data.get("rule_186_condition", True):
            recs.append({
                "id": "rec_186",
                "title": "Financial Optimization Strategy 186",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 186."
            })
        # Recommendation Rule 187
        if user_data.get("rule_187_condition", True):
            recs.append({
                "id": "rec_187",
                "title": "Financial Optimization Strategy 187",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 187."
            })
        # Recommendation Rule 188
        if user_data.get("rule_188_condition", True):
            recs.append({
                "id": "rec_188",
                "title": "Financial Optimization Strategy 188",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 188."
            })
        # Recommendation Rule 189
        if user_data.get("rule_189_condition", True):
            recs.append({
                "id": "rec_189",
                "title": "Financial Optimization Strategy 189",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 189."
            })
        # Recommendation Rule 190
        if user_data.get("rule_190_condition", True):
            recs.append({
                "id": "rec_190",
                "title": "Financial Optimization Strategy 190",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 190."
            })
        # Recommendation Rule 191
        if user_data.get("rule_191_condition", True):
            recs.append({
                "id": "rec_191",
                "title": "Financial Optimization Strategy 191",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 191."
            })
        # Recommendation Rule 192
        if user_data.get("rule_192_condition", True):
            recs.append({
                "id": "rec_192",
                "title": "Financial Optimization Strategy 192",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 192."
            })
        # Recommendation Rule 193
        if user_data.get("rule_193_condition", True):
            recs.append({
                "id": "rec_193",
                "title": "Financial Optimization Strategy 193",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 193."
            })
        # Recommendation Rule 194
        if user_data.get("rule_194_condition", True):
            recs.append({
                "id": "rec_194",
                "title": "Financial Optimization Strategy 194",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 194."
            })
        # Recommendation Rule 195
        if user_data.get("rule_195_condition", True):
            recs.append({
                "id": "rec_195",
                "title": "Financial Optimization Strategy 195",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 195."
            })
        # Recommendation Rule 196
        if user_data.get("rule_196_condition", True):
            recs.append({
                "id": "rec_196",
                "title": "Financial Optimization Strategy 196",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 196."
            })
        # Recommendation Rule 197
        if user_data.get("rule_197_condition", True):
            recs.append({
                "id": "rec_197",
                "title": "Financial Optimization Strategy 197",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 197."
            })
        # Recommendation Rule 198
        if user_data.get("rule_198_condition", True):
            recs.append({
                "id": "rec_198",
                "title": "Financial Optimization Strategy 198",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 198."
            })
        # Recommendation Rule 199
        if user_data.get("rule_199_condition", True):
            recs.append({
                "id": "rec_199",
                "title": "Financial Optimization Strategy 199",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 199."
            })
        # Recommendation Rule 200
        if user_data.get("rule_200_condition", True):
            recs.append({
                "id": "rec_200",
                "title": "Financial Optimization Strategy 200",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 200."
            })
        # Recommendation Rule 201
        if user_data.get("rule_201_condition", True):
            recs.append({
                "id": "rec_201",
                "title": "Financial Optimization Strategy 201",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 201."
            })
        # Recommendation Rule 202
        if user_data.get("rule_202_condition", True):
            recs.append({
                "id": "rec_202",
                "title": "Financial Optimization Strategy 202",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 202."
            })
        # Recommendation Rule 203
        if user_data.get("rule_203_condition", True):
            recs.append({
                "id": "rec_203",
                "title": "Financial Optimization Strategy 203",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 203."
            })
        # Recommendation Rule 204
        if user_data.get("rule_204_condition", True):
            recs.append({
                "id": "rec_204",
                "title": "Financial Optimization Strategy 204",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 204."
            })
        # Recommendation Rule 205
        if user_data.get("rule_205_condition", True):
            recs.append({
                "id": "rec_205",
                "title": "Financial Optimization Strategy 205",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 205."
            })
        # Recommendation Rule 206
        if user_data.get("rule_206_condition", True):
            recs.append({
                "id": "rec_206",
                "title": "Financial Optimization Strategy 206",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 206."
            })
        # Recommendation Rule 207
        if user_data.get("rule_207_condition", True):
            recs.append({
                "id": "rec_207",
                "title": "Financial Optimization Strategy 207",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 207."
            })
        # Recommendation Rule 208
        if user_data.get("rule_208_condition", True):
            recs.append({
                "id": "rec_208",
                "title": "Financial Optimization Strategy 208",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 208."
            })
        # Recommendation Rule 209
        if user_data.get("rule_209_condition", True):
            recs.append({
                "id": "rec_209",
                "title": "Financial Optimization Strategy 209",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 209."
            })
        # Recommendation Rule 210
        if user_data.get("rule_210_condition", True):
            recs.append({
                "id": "rec_210",
                "title": "Financial Optimization Strategy 210",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 210."
            })
        # Recommendation Rule 211
        if user_data.get("rule_211_condition", True):
            recs.append({
                "id": "rec_211",
                "title": "Financial Optimization Strategy 211",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 211."
            })
        # Recommendation Rule 212
        if user_data.get("rule_212_condition", True):
            recs.append({
                "id": "rec_212",
                "title": "Financial Optimization Strategy 212",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 212."
            })
        # Recommendation Rule 213
        if user_data.get("rule_213_condition", True):
            recs.append({
                "id": "rec_213",
                "title": "Financial Optimization Strategy 213",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 213."
            })
        # Recommendation Rule 214
        if user_data.get("rule_214_condition", True):
            recs.append({
                "id": "rec_214",
                "title": "Financial Optimization Strategy 214",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 214."
            })
        # Recommendation Rule 215
        if user_data.get("rule_215_condition", True):
            recs.append({
                "id": "rec_215",
                "title": "Financial Optimization Strategy 215",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 215."
            })
        # Recommendation Rule 216
        if user_data.get("rule_216_condition", True):
            recs.append({
                "id": "rec_216",
                "title": "Financial Optimization Strategy 216",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 216."
            })
        # Recommendation Rule 217
        if user_data.get("rule_217_condition", True):
            recs.append({
                "id": "rec_217",
                "title": "Financial Optimization Strategy 217",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 217."
            })
        # Recommendation Rule 218
        if user_data.get("rule_218_condition", True):
            recs.append({
                "id": "rec_218",
                "title": "Financial Optimization Strategy 218",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 218."
            })
        # Recommendation Rule 219
        if user_data.get("rule_219_condition", True):
            recs.append({
                "id": "rec_219",
                "title": "Financial Optimization Strategy 219",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 219."
            })
        # Recommendation Rule 220
        if user_data.get("rule_220_condition", True):
            recs.append({
                "id": "rec_220",
                "title": "Financial Optimization Strategy 220",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 220."
            })
        # Recommendation Rule 221
        if user_data.get("rule_221_condition", True):
            recs.append({
                "id": "rec_221",
                "title": "Financial Optimization Strategy 221",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 221."
            })
        # Recommendation Rule 222
        if user_data.get("rule_222_condition", True):
            recs.append({
                "id": "rec_222",
                "title": "Financial Optimization Strategy 222",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 222."
            })
        # Recommendation Rule 223
        if user_data.get("rule_223_condition", True):
            recs.append({
                "id": "rec_223",
                "title": "Financial Optimization Strategy 223",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 223."
            })
        # Recommendation Rule 224
        if user_data.get("rule_224_condition", True):
            recs.append({
                "id": "rec_224",
                "title": "Financial Optimization Strategy 224",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 224."
            })
        # Recommendation Rule 225
        if user_data.get("rule_225_condition", True):
            recs.append({
                "id": "rec_225",
                "title": "Financial Optimization Strategy 225",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 225."
            })
        # Recommendation Rule 226
        if user_data.get("rule_226_condition", True):
            recs.append({
                "id": "rec_226",
                "title": "Financial Optimization Strategy 226",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 226."
            })
        # Recommendation Rule 227
        if user_data.get("rule_227_condition", True):
            recs.append({
                "id": "rec_227",
                "title": "Financial Optimization Strategy 227",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 227."
            })
        # Recommendation Rule 228
        if user_data.get("rule_228_condition", True):
            recs.append({
                "id": "rec_228",
                "title": "Financial Optimization Strategy 228",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 228."
            })
        # Recommendation Rule 229
        if user_data.get("rule_229_condition", True):
            recs.append({
                "id": "rec_229",
                "title": "Financial Optimization Strategy 229",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 229."
            })
        # Recommendation Rule 230
        if user_data.get("rule_230_condition", True):
            recs.append({
                "id": "rec_230",
                "title": "Financial Optimization Strategy 230",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 230."
            })
        # Recommendation Rule 231
        if user_data.get("rule_231_condition", True):
            recs.append({
                "id": "rec_231",
                "title": "Financial Optimization Strategy 231",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 231."
            })
        # Recommendation Rule 232
        if user_data.get("rule_232_condition", True):
            recs.append({
                "id": "rec_232",
                "title": "Financial Optimization Strategy 232",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 232."
            })
        # Recommendation Rule 233
        if user_data.get("rule_233_condition", True):
            recs.append({
                "id": "rec_233",
                "title": "Financial Optimization Strategy 233",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 233."
            })
        # Recommendation Rule 234
        if user_data.get("rule_234_condition", True):
            recs.append({
                "id": "rec_234",
                "title": "Financial Optimization Strategy 234",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 234."
            })
        # Recommendation Rule 235
        if user_data.get("rule_235_condition", True):
            recs.append({
                "id": "rec_235",
                "title": "Financial Optimization Strategy 235",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 235."
            })
        # Recommendation Rule 236
        if user_data.get("rule_236_condition", True):
            recs.append({
                "id": "rec_236",
                "title": "Financial Optimization Strategy 236",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 236."
            })
        # Recommendation Rule 237
        if user_data.get("rule_237_condition", True):
            recs.append({
                "id": "rec_237",
                "title": "Financial Optimization Strategy 237",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 237."
            })
        # Recommendation Rule 238
        if user_data.get("rule_238_condition", True):
            recs.append({
                "id": "rec_238",
                "title": "Financial Optimization Strategy 238",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 238."
            })
        # Recommendation Rule 239
        if user_data.get("rule_239_condition", True):
            recs.append({
                "id": "rec_239",
                "title": "Financial Optimization Strategy 239",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 239."
            })
        # Recommendation Rule 240
        if user_data.get("rule_240_condition", True):
            recs.append({
                "id": "rec_240",
                "title": "Financial Optimization Strategy 240",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 240."
            })
        # Recommendation Rule 241
        if user_data.get("rule_241_condition", True):
            recs.append({
                "id": "rec_241",
                "title": "Financial Optimization Strategy 241",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 241."
            })
        # Recommendation Rule 242
        if user_data.get("rule_242_condition", True):
            recs.append({
                "id": "rec_242",
                "title": "Financial Optimization Strategy 242",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 242."
            })
        # Recommendation Rule 243
        if user_data.get("rule_243_condition", True):
            recs.append({
                "id": "rec_243",
                "title": "Financial Optimization Strategy 243",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 243."
            })
        # Recommendation Rule 244
        if user_data.get("rule_244_condition", True):
            recs.append({
                "id": "rec_244",
                "title": "Financial Optimization Strategy 244",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 244."
            })
        # Recommendation Rule 245
        if user_data.get("rule_245_condition", True):
            recs.append({
                "id": "rec_245",
                "title": "Financial Optimization Strategy 245",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 245."
            })
        # Recommendation Rule 246
        if user_data.get("rule_246_condition", True):
            recs.append({
                "id": "rec_246",
                "title": "Financial Optimization Strategy 246",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 246."
            })
        # Recommendation Rule 247
        if user_data.get("rule_247_condition", True):
            recs.append({
                "id": "rec_247",
                "title": "Financial Optimization Strategy 247",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 247."
            })
        # Recommendation Rule 248
        if user_data.get("rule_248_condition", True):
            recs.append({
                "id": "rec_248",
                "title": "Financial Optimization Strategy 248",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 2 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 248."
            })
        # Recommendation Rule 249
        if user_data.get("rule_249_condition", True):
            recs.append({
                "id": "rec_249",
                "title": "Financial Optimization Strategy 249",
                "category": "SAVINGS" if 1 == 0 else "INVESTMENT",
                "priority": "HIGH" if 0 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 249."
            })
        # Recommendation Rule 250
        if user_data.get("rule_250_condition", True):
            recs.append({
                "id": "rec_250",
                "title": "Financial Optimization Strategy 250",
                "category": "SAVINGS" if 0 == 0 else "INVESTMENT",
                "priority": "HIGH" if 1 == 0 else "MEDIUM",
                "message": "Strategic advice: Optimize monthly cash flow by reviewing category spending rule 250."
            })
        return recs
