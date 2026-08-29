"""
Comprehensive Technical Support Diagnostics Dialogue Tree.
"""

TECHNICAL_DIALOGUE_TREE = {
    "tech_step_1": {
        "step_id": 1,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 1: Is HTTP Status Code #401 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_2",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_2": {
        "step_id": 2,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 2: Is HTTP Status Code #402 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_3",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_3": {
        "step_id": 3,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 3: Is HTTP Status Code #403 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_4",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_4": {
        "step_id": 4,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 4: Is HTTP Status Code #404 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_5",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_5": {
        "step_id": 5,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 5: Is HTTP Status Code #405 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_6",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_6": {
        "step_id": 6,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 6: Is HTTP Status Code #406 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_7",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_7": {
        "step_id": 7,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 7: Is HTTP Status Code #407 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_8",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_8": {
        "step_id": 8,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 8: Is HTTP Status Code #408 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_9",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_9": {
        "step_id": 9,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 9: Is HTTP Status Code #409 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_10",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_10": {
        "step_id": 10,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 10: Is HTTP Status Code #410 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_11",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_11": {
        "step_id": 11,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 11: Is HTTP Status Code #411 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_12",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_12": {
        "step_id": 12,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 12: Is HTTP Status Code #412 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_13",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_13": {
        "step_id": 13,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 13: Is HTTP Status Code #413 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_14",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_14": {
        "step_id": 14,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 14: Is HTTP Status Code #414 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_15",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_15": {
        "step_id": 15,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 15: Is HTTP Status Code #415 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_16",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_16": {
        "step_id": 16,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 16: Is HTTP Status Code #416 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_17",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_17": {
        "step_id": 17,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 17: Is HTTP Status Code #417 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_18",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_18": {
        "step_id": 18,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 18: Is HTTP Status Code #418 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_19",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_19": {
        "step_id": 19,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 19: Is HTTP Status Code #419 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_20",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_20": {
        "step_id": 20,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 20: Is HTTP Status Code #420 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_21",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_21": {
        "step_id": 21,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 21: Is HTTP Status Code #421 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_22",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_22": {
        "step_id": 22,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 22: Is HTTP Status Code #422 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_23",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_23": {
        "step_id": 23,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 23: Is HTTP Status Code #423 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_24",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_24": {
        "step_id": 24,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 24: Is HTTP Status Code #424 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_25",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_25": {
        "step_id": 25,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 25: Is HTTP Status Code #425 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_26",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_26": {
        "step_id": 26,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 26: Is HTTP Status Code #426 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_27",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_27": {
        "step_id": 27,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 27: Is HTTP Status Code #427 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_28",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_28": {
        "step_id": 28,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 28: Is HTTP Status Code #428 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_29",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_29": {
        "step_id": 29,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 29: Is HTTP Status Code #429 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_30",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_30": {
        "step_id": 30,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 30: Is HTTP Status Code #430 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_31",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_31": {
        "step_id": 31,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 31: Is HTTP Status Code #431 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_32",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_32": {
        "step_id": 32,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 32: Is HTTP Status Code #432 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_33",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_33": {
        "step_id": 33,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 33: Is HTTP Status Code #433 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_34",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_34": {
        "step_id": 34,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 34: Is HTTP Status Code #434 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_35",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_35": {
        "step_id": 35,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 35: Is HTTP Status Code #435 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_36",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_36": {
        "step_id": 36,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 36: Is HTTP Status Code #436 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_37",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_37": {
        "step_id": 37,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 37: Is HTTP Status Code #437 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_38",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_38": {
        "step_id": 38,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 38: Is HTTP Status Code #438 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_39",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_39": {
        "step_id": 39,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 39: Is HTTP Status Code #439 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_40",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_40": {
        "step_id": 40,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 40: Is HTTP Status Code #440 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_41",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_41": {
        "step_id": 41,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 41: Is HTTP Status Code #441 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_42",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_42": {
        "step_id": 42,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 42: Is HTTP Status Code #442 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_43",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_43": {
        "step_id": 43,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 43: Is HTTP Status Code #443 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_44",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_44": {
        "step_id": 44,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 44: Is HTTP Status Code #444 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_45",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_45": {
        "step_id": 45,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 45: Is HTTP Status Code #445 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_46",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_46": {
        "step_id": 46,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 46: Is HTTP Status Code #446 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_47",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_47": {
        "step_id": 47,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 47: Is HTTP Status Code #447 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_48",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_48": {
        "step_id": 48,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 48: Is HTTP Status Code #448 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_49",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_49": {
        "step_id": 49,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 49: Is HTTP Status Code #449 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_50",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_50": {
        "step_id": 50,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 50: Is HTTP Status Code #450 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_51",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_51": {
        "step_id": 51,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 51: Is HTTP Status Code #451 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_52",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_52": {
        "step_id": 52,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 52: Is HTTP Status Code #452 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_53",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_53": {
        "step_id": 53,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 53: Is HTTP Status Code #453 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_54",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_54": {
        "step_id": 54,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 54: Is HTTP Status Code #454 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_55",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_55": {
        "step_id": 55,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 55: Is HTTP Status Code #455 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_56",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_56": {
        "step_id": 56,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 56: Is HTTP Status Code #456 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_57",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_57": {
        "step_id": 57,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 57: Is HTTP Status Code #457 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_58",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_58": {
        "step_id": 58,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 58: Is HTTP Status Code #458 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_59",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_59": {
        "step_id": 59,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 59: Is HTTP Status Code #459 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_60",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_60": {
        "step_id": 60,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 60: Is HTTP Status Code #460 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_61",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_61": {
        "step_id": 61,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 61: Is HTTP Status Code #461 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_62",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_62": {
        "step_id": 62,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 62: Is HTTP Status Code #462 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_63",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_63": {
        "step_id": 63,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 63: Is HTTP Status Code #463 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_64",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_64": {
        "step_id": 64,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 64: Is HTTP Status Code #464 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_65",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_65": {
        "step_id": 65,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 65: Is HTTP Status Code #465 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_66",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_66": {
        "step_id": 66,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 66: Is HTTP Status Code #466 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_67",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_67": {
        "step_id": 67,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 67: Is HTTP Status Code #467 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_68",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_68": {
        "step_id": 68,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 68: Is HTTP Status Code #468 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_69",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_69": {
        "step_id": 69,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 69: Is HTTP Status Code #469 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_70",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_70": {
        "step_id": 70,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 70: Is HTTP Status Code #470 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_71",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_71": {
        "step_id": 71,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 71: Is HTTP Status Code #471 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_72",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_72": {
        "step_id": 72,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 72: Is HTTP Status Code #472 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_73",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_73": {
        "step_id": 73,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 73: Is HTTP Status Code #473 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_74",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_74": {
        "step_id": 74,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 74: Is HTTP Status Code #474 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_75",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_75": {
        "step_id": 75,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 75: Is HTTP Status Code #475 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_76",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_76": {
        "step_id": 76,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 76: Is HTTP Status Code #476 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_77",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_77": {
        "step_id": 77,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 77: Is HTTP Status Code #477 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_78",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_78": {
        "step_id": 78,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 78: Is HTTP Status Code #478 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_79",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_79": {
        "step_id": 79,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 79: Is HTTP Status Code #479 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_80",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_80": {
        "step_id": 80,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 80: Is HTTP Status Code #480 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_81",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_81": {
        "step_id": 81,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 81: Is HTTP Status Code #481 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_82",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_82": {
        "step_id": 82,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 82: Is HTTP Status Code #482 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_83",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_83": {
        "step_id": 83,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 83: Is HTTP Status Code #483 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_84",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_84": {
        "step_id": 84,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 84: Is HTTP Status Code #484 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_85",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_85": {
        "step_id": 85,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 85: Is HTTP Status Code #485 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_86",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_86": {
        "step_id": 86,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 86: Is HTTP Status Code #486 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_87",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_87": {
        "step_id": 87,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 87: Is HTTP Status Code #487 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_88",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_88": {
        "step_id": 88,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 88: Is HTTP Status Code #488 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_89",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_89": {
        "step_id": 89,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 89: Is HTTP Status Code #489 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_90",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_90": {
        "step_id": 90,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 90: Is HTTP Status Code #490 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_91",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_91": {
        "step_id": 91,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 91: Is HTTP Status Code #491 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_92",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_92": {
        "step_id": 92,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 92: Is HTTP Status Code #492 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_93",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_93": {
        "step_id": 93,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 93: Is HTTP Status Code #493 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_94",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_94": {
        "step_id": 94,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 94: Is HTTP Status Code #494 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_95",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_95": {
        "step_id": 95,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 95: Is HTTP Status Code #495 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_96",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_96": {
        "step_id": 96,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 96: Is HTTP Status Code #496 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_97",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_97": {
        "step_id": 97,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 97: Is HTTP Status Code #497 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_98",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_98": {
        "step_id": 98,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 98: Is HTTP Status Code #498 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_99",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_99": {
        "step_id": 99,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 99: Is HTTP Status Code #499 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_100",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_100": {
        "step_id": 100,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 100: Is HTTP Status Code #500 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_101",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_101": {
        "step_id": 101,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 101: Is HTTP Status Code #501 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_102",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_102": {
        "step_id": 102,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 102: Is HTTP Status Code #502 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_103",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_103": {
        "step_id": 103,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 103: Is HTTP Status Code #503 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_104",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_104": {
        "step_id": 104,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 104: Is HTTP Status Code #504 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_105",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_105": {
        "step_id": 105,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 105: Is HTTP Status Code #505 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_106",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_106": {
        "step_id": 106,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 106: Is HTTP Status Code #506 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_107",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_107": {
        "step_id": 107,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 107: Is HTTP Status Code #507 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_108",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_108": {
        "step_id": 108,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 108: Is HTTP Status Code #508 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_109",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_109": {
        "step_id": 109,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 109: Is HTTP Status Code #509 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_110",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_110": {
        "step_id": 110,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 110: Is HTTP Status Code #510 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_111",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_111": {
        "step_id": 111,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 111: Is HTTP Status Code #511 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_112",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_112": {
        "step_id": 112,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 112: Is HTTP Status Code #512 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_113",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_113": {
        "step_id": 113,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 113: Is HTTP Status Code #513 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_114",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_114": {
        "step_id": 114,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 114: Is HTTP Status Code #514 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_115",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_115": {
        "step_id": 115,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 115: Is HTTP Status Code #515 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_116",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_116": {
        "step_id": 116,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 116: Is HTTP Status Code #516 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_117",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_117": {
        "step_id": 117,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 117: Is HTTP Status Code #517 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_118",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_118": {
        "step_id": 118,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 118: Is HTTP Status Code #518 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_119",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_119": {
        "step_id": 119,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 119: Is HTTP Status Code #519 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_120",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_120": {
        "step_id": 120,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 120: Is HTTP Status Code #520 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_121",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_121": {
        "step_id": 121,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 121: Is HTTP Status Code #521 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_122",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_122": {
        "step_id": 122,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 122: Is HTTP Status Code #522 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_123",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_123": {
        "step_id": 123,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 123: Is HTTP Status Code #523 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_124",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_124": {
        "step_id": 124,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 124: Is HTTP Status Code #524 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_125",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_125": {
        "step_id": 125,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 125: Is HTTP Status Code #525 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_126",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_126": {
        "step_id": 126,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 126: Is HTTP Status Code #526 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_127",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_127": {
        "step_id": 127,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 127: Is HTTP Status Code #527 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_128",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_128": {
        "step_id": 128,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 128: Is HTTP Status Code #528 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_129",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_129": {
        "step_id": 129,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 129: Is HTTP Status Code #529 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_130",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_130": {
        "step_id": 130,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 130: Is HTTP Status Code #530 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_131",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_131": {
        "step_id": 131,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 131: Is HTTP Status Code #531 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_132",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_132": {
        "step_id": 132,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 132: Is HTTP Status Code #532 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_133",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_133": {
        "step_id": 133,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 133: Is HTTP Status Code #533 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_134",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_134": {
        "step_id": 134,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 134: Is HTTP Status Code #534 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_135",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_135": {
        "step_id": 135,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 135: Is HTTP Status Code #535 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_136",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_136": {
        "step_id": 136,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 136: Is HTTP Status Code #536 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_137",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_137": {
        "step_id": 137,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 137: Is HTTP Status Code #537 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_138",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_138": {
        "step_id": 138,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 138: Is HTTP Status Code #538 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_139",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_139": {
        "step_id": 139,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 139: Is HTTP Status Code #539 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_140",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_140": {
        "step_id": 140,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 140: Is HTTP Status Code #540 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_141",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_141": {
        "step_id": 141,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 141: Is HTTP Status Code #541 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_142",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_142": {
        "step_id": 142,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 142: Is HTTP Status Code #542 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_143",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_143": {
        "step_id": 143,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 143: Is HTTP Status Code #543 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_144",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_144": {
        "step_id": 144,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 144: Is HTTP Status Code #544 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_145",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_145": {
        "step_id": 145,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 145: Is HTTP Status Code #545 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_146",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_146": {
        "step_id": 146,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 146: Is HTTP Status Code #546 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_147",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_147": {
        "step_id": 147,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 147: Is HTTP Status Code #547 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_148",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_148": {
        "step_id": 148,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 148: Is HTTP Status Code #548 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_149",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_149": {
        "step_id": 149,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 149: Is HTTP Status Code #549 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_150",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
    "tech_step_150": {
        "step_id": 150,
        "node_type": "diagnostic",
        "prompt": "Technical Diagnostic step 150: Is HTTP Status Code #550 observed in your browser console?",
        "options": ["Confirmed Yes", "Different Code", "Not Sure"],
        "next_step_yes": "tech_step_151",
        "next_step_no": "tech_general_handler",
        "recommended_action": "Check system diagnostics endpoint at /diagnostics"
    },
}
