"""
Comprehensive Billing Dialogue Decision Tree Flow.
"""

BILLING_DIALOGUE_TREE = {
    "billing_step_1": {
        "step_id": 1,
        "node_type": "decision",
        "prompt": "Billing verification step 1: Have you reviewed line item #1 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_2",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_2": {
        "step_id": 2,
        "node_type": "decision",
        "prompt": "Billing verification step 2: Have you reviewed line item #2 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_3",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_3": {
        "step_id": 3,
        "node_type": "decision",
        "prompt": "Billing verification step 3: Have you reviewed line item #3 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_4",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_4": {
        "step_id": 4,
        "node_type": "decision",
        "prompt": "Billing verification step 4: Have you reviewed line item #4 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_5",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_5": {
        "step_id": 5,
        "node_type": "decision",
        "prompt": "Billing verification step 5: Have you reviewed line item #5 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_6",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_6": {
        "step_id": 6,
        "node_type": "decision",
        "prompt": "Billing verification step 6: Have you reviewed line item #6 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_7",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_7": {
        "step_id": 7,
        "node_type": "decision",
        "prompt": "Billing verification step 7: Have you reviewed line item #7 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_8",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_8": {
        "step_id": 8,
        "node_type": "decision",
        "prompt": "Billing verification step 8: Have you reviewed line item #8 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_9",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_9": {
        "step_id": 9,
        "node_type": "decision",
        "prompt": "Billing verification step 9: Have you reviewed line item #9 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_10",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_10": {
        "step_id": 10,
        "node_type": "decision",
        "prompt": "Billing verification step 10: Have you reviewed line item #10 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_11",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_11": {
        "step_id": 11,
        "node_type": "decision",
        "prompt": "Billing verification step 11: Have you reviewed line item #11 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_12",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_12": {
        "step_id": 12,
        "node_type": "decision",
        "prompt": "Billing verification step 12: Have you reviewed line item #12 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_13",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_13": {
        "step_id": 13,
        "node_type": "decision",
        "prompt": "Billing verification step 13: Have you reviewed line item #13 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_14",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_14": {
        "step_id": 14,
        "node_type": "decision",
        "prompt": "Billing verification step 14: Have you reviewed line item #14 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_15",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_15": {
        "step_id": 15,
        "node_type": "decision",
        "prompt": "Billing verification step 15: Have you reviewed line item #15 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_16",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_16": {
        "step_id": 16,
        "node_type": "decision",
        "prompt": "Billing verification step 16: Have you reviewed line item #16 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_17",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_17": {
        "step_id": 17,
        "node_type": "decision",
        "prompt": "Billing verification step 17: Have you reviewed line item #17 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_18",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_18": {
        "step_id": 18,
        "node_type": "decision",
        "prompt": "Billing verification step 18: Have you reviewed line item #18 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_19",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_19": {
        "step_id": 19,
        "node_type": "decision",
        "prompt": "Billing verification step 19: Have you reviewed line item #19 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_20",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_20": {
        "step_id": 20,
        "node_type": "decision",
        "prompt": "Billing verification step 20: Have you reviewed line item #20 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_21",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_21": {
        "step_id": 21,
        "node_type": "decision",
        "prompt": "Billing verification step 21: Have you reviewed line item #21 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_22",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_22": {
        "step_id": 22,
        "node_type": "decision",
        "prompt": "Billing verification step 22: Have you reviewed line item #22 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_23",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_23": {
        "step_id": 23,
        "node_type": "decision",
        "prompt": "Billing verification step 23: Have you reviewed line item #23 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_24",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_24": {
        "step_id": 24,
        "node_type": "decision",
        "prompt": "Billing verification step 24: Have you reviewed line item #24 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_25",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_25": {
        "step_id": 25,
        "node_type": "decision",
        "prompt": "Billing verification step 25: Have you reviewed line item #25 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_26",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_26": {
        "step_id": 26,
        "node_type": "decision",
        "prompt": "Billing verification step 26: Have you reviewed line item #26 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_27",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_27": {
        "step_id": 27,
        "node_type": "decision",
        "prompt": "Billing verification step 27: Have you reviewed line item #27 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_28",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_28": {
        "step_id": 28,
        "node_type": "decision",
        "prompt": "Billing verification step 28: Have you reviewed line item #28 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_29",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_29": {
        "step_id": 29,
        "node_type": "decision",
        "prompt": "Billing verification step 29: Have you reviewed line item #29 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_30",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_30": {
        "step_id": 30,
        "node_type": "decision",
        "prompt": "Billing verification step 30: Have you reviewed line item #30 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_31",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_31": {
        "step_id": 31,
        "node_type": "decision",
        "prompt": "Billing verification step 31: Have you reviewed line item #31 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_32",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_32": {
        "step_id": 32,
        "node_type": "decision",
        "prompt": "Billing verification step 32: Have you reviewed line item #32 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_33",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_33": {
        "step_id": 33,
        "node_type": "decision",
        "prompt": "Billing verification step 33: Have you reviewed line item #33 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_34",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_34": {
        "step_id": 34,
        "node_type": "decision",
        "prompt": "Billing verification step 34: Have you reviewed line item #34 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_35",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_35": {
        "step_id": 35,
        "node_type": "decision",
        "prompt": "Billing verification step 35: Have you reviewed line item #35 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_36",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_36": {
        "step_id": 36,
        "node_type": "decision",
        "prompt": "Billing verification step 36: Have you reviewed line item #36 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_37",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_37": {
        "step_id": 37,
        "node_type": "decision",
        "prompt": "Billing verification step 37: Have you reviewed line item #37 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_38",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_38": {
        "step_id": 38,
        "node_type": "decision",
        "prompt": "Billing verification step 38: Have you reviewed line item #38 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_39",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_39": {
        "step_id": 39,
        "node_type": "decision",
        "prompt": "Billing verification step 39: Have you reviewed line item #39 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_40",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_40": {
        "step_id": 40,
        "node_type": "decision",
        "prompt": "Billing verification step 40: Have you reviewed line item #40 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_41",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_41": {
        "step_id": 41,
        "node_type": "decision",
        "prompt": "Billing verification step 41: Have you reviewed line item #41 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_42",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_42": {
        "step_id": 42,
        "node_type": "decision",
        "prompt": "Billing verification step 42: Have you reviewed line item #42 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_43",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_43": {
        "step_id": 43,
        "node_type": "decision",
        "prompt": "Billing verification step 43: Have you reviewed line item #43 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_44",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_44": {
        "step_id": 44,
        "node_type": "decision",
        "prompt": "Billing verification step 44: Have you reviewed line item #44 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_45",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_45": {
        "step_id": 45,
        "node_type": "decision",
        "prompt": "Billing verification step 45: Have you reviewed line item #45 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_46",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_46": {
        "step_id": 46,
        "node_type": "decision",
        "prompt": "Billing verification step 46: Have you reviewed line item #46 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_47",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_47": {
        "step_id": 47,
        "node_type": "decision",
        "prompt": "Billing verification step 47: Have you reviewed line item #47 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_48",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_48": {
        "step_id": 48,
        "node_type": "decision",
        "prompt": "Billing verification step 48: Have you reviewed line item #48 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_49",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_49": {
        "step_id": 49,
        "node_type": "decision",
        "prompt": "Billing verification step 49: Have you reviewed line item #49 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_50",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_50": {
        "step_id": 50,
        "node_type": "decision",
        "prompt": "Billing verification step 50: Have you reviewed line item #50 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_51",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_51": {
        "step_id": 51,
        "node_type": "decision",
        "prompt": "Billing verification step 51: Have you reviewed line item #51 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_52",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_52": {
        "step_id": 52,
        "node_type": "decision",
        "prompt": "Billing verification step 52: Have you reviewed line item #52 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_53",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_53": {
        "step_id": 53,
        "node_type": "decision",
        "prompt": "Billing verification step 53: Have you reviewed line item #53 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_54",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_54": {
        "step_id": 54,
        "node_type": "decision",
        "prompt": "Billing verification step 54: Have you reviewed line item #54 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_55",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_55": {
        "step_id": 55,
        "node_type": "decision",
        "prompt": "Billing verification step 55: Have you reviewed line item #55 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_56",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_56": {
        "step_id": 56,
        "node_type": "decision",
        "prompt": "Billing verification step 56: Have you reviewed line item #56 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_57",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_57": {
        "step_id": 57,
        "node_type": "decision",
        "prompt": "Billing verification step 57: Have you reviewed line item #57 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_58",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_58": {
        "step_id": 58,
        "node_type": "decision",
        "prompt": "Billing verification step 58: Have you reviewed line item #58 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_59",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_59": {
        "step_id": 59,
        "node_type": "decision",
        "prompt": "Billing verification step 59: Have you reviewed line item #59 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_60",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_60": {
        "step_id": 60,
        "node_type": "decision",
        "prompt": "Billing verification step 60: Have you reviewed line item #60 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_61",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_61": {
        "step_id": 61,
        "node_type": "decision",
        "prompt": "Billing verification step 61: Have you reviewed line item #61 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_62",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_62": {
        "step_id": 62,
        "node_type": "decision",
        "prompt": "Billing verification step 62: Have you reviewed line item #62 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_63",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_63": {
        "step_id": 63,
        "node_type": "decision",
        "prompt": "Billing verification step 63: Have you reviewed line item #63 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_64",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_64": {
        "step_id": 64,
        "node_type": "decision",
        "prompt": "Billing verification step 64: Have you reviewed line item #64 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_65",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_65": {
        "step_id": 65,
        "node_type": "decision",
        "prompt": "Billing verification step 65: Have you reviewed line item #65 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_66",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_66": {
        "step_id": 66,
        "node_type": "decision",
        "prompt": "Billing verification step 66: Have you reviewed line item #66 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_67",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_67": {
        "step_id": 67,
        "node_type": "decision",
        "prompt": "Billing verification step 67: Have you reviewed line item #67 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_68",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_68": {
        "step_id": 68,
        "node_type": "decision",
        "prompt": "Billing verification step 68: Have you reviewed line item #68 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_69",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_69": {
        "step_id": 69,
        "node_type": "decision",
        "prompt": "Billing verification step 69: Have you reviewed line item #69 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_70",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_70": {
        "step_id": 70,
        "node_type": "decision",
        "prompt": "Billing verification step 70: Have you reviewed line item #70 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_71",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_71": {
        "step_id": 71,
        "node_type": "decision",
        "prompt": "Billing verification step 71: Have you reviewed line item #71 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_72",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_72": {
        "step_id": 72,
        "node_type": "decision",
        "prompt": "Billing verification step 72: Have you reviewed line item #72 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_73",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_73": {
        "step_id": 73,
        "node_type": "decision",
        "prompt": "Billing verification step 73: Have you reviewed line item #73 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_74",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_74": {
        "step_id": 74,
        "node_type": "decision",
        "prompt": "Billing verification step 74: Have you reviewed line item #74 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_75",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_75": {
        "step_id": 75,
        "node_type": "decision",
        "prompt": "Billing verification step 75: Have you reviewed line item #75 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_76",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_76": {
        "step_id": 76,
        "node_type": "decision",
        "prompt": "Billing verification step 76: Have you reviewed line item #76 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_77",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_77": {
        "step_id": 77,
        "node_type": "decision",
        "prompt": "Billing verification step 77: Have you reviewed line item #77 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_78",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_78": {
        "step_id": 78,
        "node_type": "decision",
        "prompt": "Billing verification step 78: Have you reviewed line item #78 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_79",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_79": {
        "step_id": 79,
        "node_type": "decision",
        "prompt": "Billing verification step 79: Have you reviewed line item #79 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_80",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_80": {
        "step_id": 80,
        "node_type": "decision",
        "prompt": "Billing verification step 80: Have you reviewed line item #80 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_81",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_81": {
        "step_id": 81,
        "node_type": "decision",
        "prompt": "Billing verification step 81: Have you reviewed line item #81 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_82",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_82": {
        "step_id": 82,
        "node_type": "decision",
        "prompt": "Billing verification step 82: Have you reviewed line item #82 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_83",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_83": {
        "step_id": 83,
        "node_type": "decision",
        "prompt": "Billing verification step 83: Have you reviewed line item #83 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_84",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_84": {
        "step_id": 84,
        "node_type": "decision",
        "prompt": "Billing verification step 84: Have you reviewed line item #84 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_85",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_85": {
        "step_id": 85,
        "node_type": "decision",
        "prompt": "Billing verification step 85: Have you reviewed line item #85 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_86",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_86": {
        "step_id": 86,
        "node_type": "decision",
        "prompt": "Billing verification step 86: Have you reviewed line item #86 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_87",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_87": {
        "step_id": 87,
        "node_type": "decision",
        "prompt": "Billing verification step 87: Have you reviewed line item #87 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_88",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_88": {
        "step_id": 88,
        "node_type": "decision",
        "prompt": "Billing verification step 88: Have you reviewed line item #88 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_89",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_89": {
        "step_id": 89,
        "node_type": "decision",
        "prompt": "Billing verification step 89: Have you reviewed line item #89 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_90",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_90": {
        "step_id": 90,
        "node_type": "decision",
        "prompt": "Billing verification step 90: Have you reviewed line item #90 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_91",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_91": {
        "step_id": 91,
        "node_type": "decision",
        "prompt": "Billing verification step 91: Have you reviewed line item #91 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_92",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_92": {
        "step_id": 92,
        "node_type": "decision",
        "prompt": "Billing verification step 92: Have you reviewed line item #92 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_93",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_93": {
        "step_id": 93,
        "node_type": "decision",
        "prompt": "Billing verification step 93: Have you reviewed line item #93 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_94",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_94": {
        "step_id": 94,
        "node_type": "decision",
        "prompt": "Billing verification step 94: Have you reviewed line item #94 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_95",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_95": {
        "step_id": 95,
        "node_type": "decision",
        "prompt": "Billing verification step 95: Have you reviewed line item #95 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_96",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_96": {
        "step_id": 96,
        "node_type": "decision",
        "prompt": "Billing verification step 96: Have you reviewed line item #96 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_97",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_97": {
        "step_id": 97,
        "node_type": "decision",
        "prompt": "Billing verification step 97: Have you reviewed line item #97 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_98",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_98": {
        "step_id": 98,
        "node_type": "decision",
        "prompt": "Billing verification step 98: Have you reviewed line item #98 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_99",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_99": {
        "step_id": 99,
        "node_type": "decision",
        "prompt": "Billing verification step 99: Have you reviewed line item #99 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_100",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_100": {
        "step_id": 100,
        "node_type": "decision",
        "prompt": "Billing verification step 100: Have you reviewed line item #100 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_101",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_101": {
        "step_id": 101,
        "node_type": "decision",
        "prompt": "Billing verification step 101: Have you reviewed line item #101 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_102",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_102": {
        "step_id": 102,
        "node_type": "decision",
        "prompt": "Billing verification step 102: Have you reviewed line item #102 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_103",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_103": {
        "step_id": 103,
        "node_type": "decision",
        "prompt": "Billing verification step 103: Have you reviewed line item #103 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_104",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_104": {
        "step_id": 104,
        "node_type": "decision",
        "prompt": "Billing verification step 104: Have you reviewed line item #104 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_105",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_105": {
        "step_id": 105,
        "node_type": "decision",
        "prompt": "Billing verification step 105: Have you reviewed line item #105 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_106",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_106": {
        "step_id": 106,
        "node_type": "decision",
        "prompt": "Billing verification step 106: Have you reviewed line item #106 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_107",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_107": {
        "step_id": 107,
        "node_type": "decision",
        "prompt": "Billing verification step 107: Have you reviewed line item #107 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_108",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_108": {
        "step_id": 108,
        "node_type": "decision",
        "prompt": "Billing verification step 108: Have you reviewed line item #108 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_109",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_109": {
        "step_id": 109,
        "node_type": "decision",
        "prompt": "Billing verification step 109: Have you reviewed line item #109 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_110",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_110": {
        "step_id": 110,
        "node_type": "decision",
        "prompt": "Billing verification step 110: Have you reviewed line item #110 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_111",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_111": {
        "step_id": 111,
        "node_type": "decision",
        "prompt": "Billing verification step 111: Have you reviewed line item #111 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_112",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_112": {
        "step_id": 112,
        "node_type": "decision",
        "prompt": "Billing verification step 112: Have you reviewed line item #112 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_113",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_113": {
        "step_id": 113,
        "node_type": "decision",
        "prompt": "Billing verification step 113: Have you reviewed line item #113 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_114",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_114": {
        "step_id": 114,
        "node_type": "decision",
        "prompt": "Billing verification step 114: Have you reviewed line item #114 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_115",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_115": {
        "step_id": 115,
        "node_type": "decision",
        "prompt": "Billing verification step 115: Have you reviewed line item #115 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_116",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_116": {
        "step_id": 116,
        "node_type": "decision",
        "prompt": "Billing verification step 116: Have you reviewed line item #116 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_117",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_117": {
        "step_id": 117,
        "node_type": "decision",
        "prompt": "Billing verification step 117: Have you reviewed line item #117 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_118",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_118": {
        "step_id": 118,
        "node_type": "decision",
        "prompt": "Billing verification step 118: Have you reviewed line item #118 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_119",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_119": {
        "step_id": 119,
        "node_type": "decision",
        "prompt": "Billing verification step 119: Have you reviewed line item #119 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_120",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_120": {
        "step_id": 120,
        "node_type": "decision",
        "prompt": "Billing verification step 120: Have you reviewed line item #120 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_121",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_121": {
        "step_id": 121,
        "node_type": "decision",
        "prompt": "Billing verification step 121: Have you reviewed line item #121 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_122",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_122": {
        "step_id": 122,
        "node_type": "decision",
        "prompt": "Billing verification step 122: Have you reviewed line item #122 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_123",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_123": {
        "step_id": 123,
        "node_type": "decision",
        "prompt": "Billing verification step 123: Have you reviewed line item #123 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_124",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_124": {
        "step_id": 124,
        "node_type": "decision",
        "prompt": "Billing verification step 124: Have you reviewed line item #124 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_125",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_125": {
        "step_id": 125,
        "node_type": "decision",
        "prompt": "Billing verification step 125: Have you reviewed line item #125 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_126",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_126": {
        "step_id": 126,
        "node_type": "decision",
        "prompt": "Billing verification step 126: Have you reviewed line item #126 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_127",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_127": {
        "step_id": 127,
        "node_type": "decision",
        "prompt": "Billing verification step 127: Have you reviewed line item #127 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_128",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_128": {
        "step_id": 128,
        "node_type": "decision",
        "prompt": "Billing verification step 128: Have you reviewed line item #128 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_129",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_129": {
        "step_id": 129,
        "node_type": "decision",
        "prompt": "Billing verification step 129: Have you reviewed line item #129 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_130",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_130": {
        "step_id": 130,
        "node_type": "decision",
        "prompt": "Billing verification step 130: Have you reviewed line item #130 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_131",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_131": {
        "step_id": 131,
        "node_type": "decision",
        "prompt": "Billing verification step 131: Have you reviewed line item #131 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_132",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_132": {
        "step_id": 132,
        "node_type": "decision",
        "prompt": "Billing verification step 132: Have you reviewed line item #132 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_133",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_133": {
        "step_id": 133,
        "node_type": "decision",
        "prompt": "Billing verification step 133: Have you reviewed line item #133 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_134",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_134": {
        "step_id": 134,
        "node_type": "decision",
        "prompt": "Billing verification step 134: Have you reviewed line item #134 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_135",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_135": {
        "step_id": 135,
        "node_type": "decision",
        "prompt": "Billing verification step 135: Have you reviewed line item #135 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_136",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_136": {
        "step_id": 136,
        "node_type": "decision",
        "prompt": "Billing verification step 136: Have you reviewed line item #136 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_137",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_137": {
        "step_id": 137,
        "node_type": "decision",
        "prompt": "Billing verification step 137: Have you reviewed line item #137 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_138",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_138": {
        "step_id": 138,
        "node_type": "decision",
        "prompt": "Billing verification step 138: Have you reviewed line item #138 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_139",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_139": {
        "step_id": 139,
        "node_type": "decision",
        "prompt": "Billing verification step 139: Have you reviewed line item #139 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_140",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_140": {
        "step_id": 140,
        "node_type": "decision",
        "prompt": "Billing verification step 140: Have you reviewed line item #140 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_141",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
    "billing_step_141": {
        "step_id": 141,
        "node_type": "decision",
        "prompt": "Billing verification step 141: Have you reviewed line item #141 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_142",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-2"
    },
    "billing_step_142": {
        "step_id": 142,
        "node_type": "decision",
        "prompt": "Billing verification step 142: Have you reviewed line item #142 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_143",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-3"
    },
    "billing_step_143": {
        "step_id": 143,
        "node_type": "decision",
        "prompt": "Billing verification step 143: Have you reviewed line item #143 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_144",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-4"
    },
    "billing_step_144": {
        "step_id": 144,
        "node_type": "decision",
        "prompt": "Billing verification step 144: Have you reviewed line item #144 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_145",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-5"
    },
    "billing_step_145": {
        "step_id": 145,
        "node_type": "decision",
        "prompt": "Billing verification step 145: Have you reviewed line item #145 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_146",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-6"
    },
    "billing_step_146": {
        "step_id": 146,
        "node_type": "decision",
        "prompt": "Billing verification step 146: Have you reviewed line item #146 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_147",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-7"
    },
    "billing_step_147": {
        "step_id": 147,
        "node_type": "decision",
        "prompt": "Billing verification step 147: Have you reviewed line item #147 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_148",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-8"
    },
    "billing_step_148": {
        "step_id": 148,
        "node_type": "decision",
        "prompt": "Billing verification step 148: Have you reviewed line item #148 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_149",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-9"
    },
    "billing_step_149": {
        "step_id": 149,
        "node_type": "decision",
        "prompt": "Billing verification step 149: Have you reviewed line item #149 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_150",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-10"
    },
    "billing_step_150": {
        "step_id": 150,
        "node_type": "decision",
        "prompt": "Billing verification step 150: Have you reviewed line item #150 on your monthly invoice?",
        "options": ["Yes, verified", "No, discrepancy noticed", "Escalate to agent"],
        "next_step_yes": "billing_step_151",
        "next_step_no": "billing_discrepancy_handler",
        "help_article_id": "art-billing-1"
    },
}
